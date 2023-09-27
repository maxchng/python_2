from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff(path):
    """Take a csv file and save it into a new png file called graph."""
    df = load(path)
    if df is None:
        print("You have given a wrong path!")
        return None
    years = df.columns[1:]
    values = df.iloc[123][1:]
    graph = pd.DataFrame(values, years)
    graph.plot(title="Malaysia Life expectancy Projections",
               xlabel="Year",
               ylabel="Life expectancy",
               legend=False)
    plt.savefig("graph.png")


if __name__ == "__main__":
    aff("life_expectancy_years.csv")
