import pandas as pd
import numpy as np

from duckduckgo_search import ddg
from tldextract import extract
from time import sleep

bias_map = {
    "left": -2,
    "left-center": -1,
    "center": 0,
    "right-center": 1,
    "right": 2
}

def get_url(outlet):
    results = ddg(outlet, region='en-us', max_results=1)
    return results[0]["href"] if len(results) >= 1 else ''

def strip_url(full_url):
    r = extract(full_url)
    return '.'.join([r.domain, r.suffix])

def get_logistic(x_med, x_min, lo):
    """Compute the logistic function such that
    x_min is mapped to lo and x_med is mapped to 0.5"""
    k = np.log(1 / lo) / (x_med - x_min)
    return lambda x: 1 / (1 + np.exp(-k * (x - x_med)))

if __name__ == "__main__":
    df_mb = pd.read_csv("allsides_dirty.csv")

    # Remove allsides outlets
    df_mb = df_mb[df_mb["bias"] != "allsides"]
    
    # Map bias to numbers
    df_mb["bias"] = df_mb["bias"].map(bias_map)
    
    # Weight outlets according to how certain the bias rating is
    df_mb["agree_coef"] = df_mb["total_votes"] * df_mb["agree_ratio"]
    
    # Minimum will have a weight of 0.1
    lo = 0.1
    x_med = df_mb["agree_coef"].median()
    x_min = df_mb["agree_coef"].min()
    S = get_logistic(x_med, x_min, lo)
    
    df_mb["weight"] = S(df_mb["agree_coef"])
    
    # Keep only certain columns
    df_mb = df_mb.filter(items=["name", "bias", "weight", "total_votes", "agree_ratio"])
    
    # Get the urls for all outlets
    urls = []
    for outlet in df_mb["name"]:
        url = strip_url(get_url(outlet))
        urls.append(url)
        # DuckDuckGo restricts access when we make many requests
        sleep(1.5)

    df_mb["url"] = urls
    
    # Remove bogus entries
    df_mb = df_mb[~(df_mb["url"].str.contains("wikipedia|facebook|youtube"))]
    
    # Only keep the first one in case of duplicates
    df_mb = df_mb.drop_duplicates(subset="url")
    
    df_mb.to_csv("allsides.csv", index=False)