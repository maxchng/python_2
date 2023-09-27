import pandas as pd


def load(path: str) -> str:
    """Get the content of a csv file, and return it."""
    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        return None
    else:
        rows, cols = data.shape
        print(f"Loading dataset of dimensions {(rows, cols)}")
        df = data.to_string(index=False)
        df_str = "\n".join(line.lstrip() for line in df.split("\n"))
        return df_str

print(load("life_expectancy_years.csv"))
