import pandas as pd

def run():
    print("🧹 Cleaning orders...")

    df = pd.read_csv("data/bronze/orders.csv")

    df = df.drop_duplicates()

    df.to_csv("data/silver/orders_clean.csv", index=False)

    print("✅ orders_clean.csv generated")