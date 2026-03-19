import pandas as pd

def run():
    print("🧹 Cleaning customers...")

    df = pd.read_csv("data/bronze/customers.csv")

    df = df.drop_duplicates()

    df["email"] = df["email"].fillna("unknown")

    df.to_csv("data/silver/customers_clean.csv", index=False)

    print("✅ customers_clean.csv generated")