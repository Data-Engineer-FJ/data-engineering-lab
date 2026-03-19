import pandas as pd

def run():
    print("🧹 Cleaning products...")

    df = pd.read_csv("data/bronze/products.csv")

    df = df.drop_duplicates()

    df = df[df["price"] > 0]

    df.to_csv("data/silver/products_clean.csv", index=False)

    print("✅ products_clean.csv generated")