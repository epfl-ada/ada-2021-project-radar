from bs4 import BeautifulSoup
import csv

cefr_level_map = {
    "A1": 1,
    "A2": 2,
    "B1": 3,
    "B2": 4,
    "C1": 5,
    "C2": 6,
}

def bs_to_csv(soup, csv_writer):
    table = soup.find("tbody")
    tr_rows = table.find_all("tr")
    csv_writer.writerow(["word", "guideword", "level", "part of speech", "topic"])
    csv_writer.writerows(
        [[t.text for t in r.find_all("td")][:-1] for r in tr_rows]
    )
    
CEFR_HTML = "../data/cefr.html"
CEFR_CSV_DIRTY = "../data/cefr_dirty.csv"
CEFR_CSV = "../data/cefr.csv"

def scrape():
    # Scrape the HTML file and write in CSV format to file.
    with open(CEFR_HTML) as fp, open(CEFR_CSV_DIRTY, 'w') as csv_out:
        soup = BeautifulSoup(fp)
        csv_writer = csv.writer(csv_out, delimiter=',')
        bs_to_csv(soup, csv_writer)
    
def clean():
    df_cefr = pd.read_csv(CEFR_CSV_DIRTY)
    
    # Do not keep idioms and other multi-word expressions
    df_cefr = df_cefr[[len(w.split()) == 1 for w in df_cefr["word"]]]

    df_cefr["word"] = df_cefr["word"].transform(
        lambda w: w.lower()\
                   .translate(str.maketrans('', '', string.punctuation)))

    # Use the map to transform the level column
    df_cefr["level"] = df_cefr_copy["level"].map(cefr_level_map)

    # Aggregate with the median
    df_cefr = df_cefr.groupby("word").agg("median").reset_index()

    # Rearrange columns
    df_cefr.index = df_cefr.word
    df_cefr = df_cefr.filter(items=["level"])

    df_cefr.to_csv(CEFR_CSV)
    fig.update_layout(
        title="Plot Title",
        xaxis_title="X Axis Title",
        yaxis_title="Y Axis Title",
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

if __name__ == "__main__":
    scrape()