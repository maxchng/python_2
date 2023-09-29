from load_csv import load
import matplotlib.pyplot as plt


def projection_life(path_1, path_2):
    """Save a scatter graph"""
    df_income = load(path_1)
    df_life = load(path_2)
    if df_income is None or df_life is None:
        print("One of the path is wrong!!")
        return None
    year_income = df_income["1900"]
    year_life = df_life["1900"]
    year_life = year_life
    plt.scatter(year_income, year_life)
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.savefig("graph.png")


if __name__ == "__main__":
    projection_life("income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
                    "life_expectancy_years.csv")
