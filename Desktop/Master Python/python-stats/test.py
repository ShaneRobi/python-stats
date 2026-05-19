import pandas as pn

if __name__ == "__main__":
    df = pn.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print(df)
    print(df["a"])
    print(df["b"])
    print(df["a"] + df["b"])
    print(df["a"] * df["b"])
    print(df["a"] / df["b"])
    print(df["a"] - df["b"])
    print(df["a"].mean())
    print(df["b"].mean())
    print(df["a"].std())
    print(df["b"].std())
    print(df["a"].min())
    print(df["a"].max())
    print(df["b"].min())
    print(df["b"].max())
    print(df.describe())

    