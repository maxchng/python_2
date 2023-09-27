from load_csv import load
import matplotlib.pyplot as plt


def convert_population(val):
    """Convert the str val to float val"""
    if val.endswith("k"):
        return float(val[:-1]) * 1e3
    elif val.endswith("M"):
        return float(val[:-1]) * 1e6
    else:
        return float(val)


def ft_pop(path):
    """See the graph of 2 country"""
    df = load(path)
    if df is None:
        print("The path is wrong!")
        return None
    years = df.columns[1:252]
    malaysia_population = df.loc[df["country"] == "Malaysia"].iloc[0][1:252]
    france_population = df.loc[df["country"] == "France"].iloc[0][1:252]
    malaysia_population = malaysia_population.apply(convert_population)
    france_population = france_population.apply(convert_population)
    plt.plot(years, malaysia_population, color="blue")
    plt.plot(years, france_population, color="green")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(["Malaysia", "France"], loc="lower right")
    plt.xticks(["1800", "1850", "1900", "1950", "2000", "2050"])
    plt.yticks([20e6, 40e6, 60e6], ["20M", "40M", "60M"])
    plt.savefig("graph.png")


if __name__ == "__main__":
    ft_pop("population_total.csv")
