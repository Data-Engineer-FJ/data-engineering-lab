import pandas as pd

def run():
    print("🧹 Cleaning payments...")

    df = pd.read_csv("data/bronze/payments.csv")

    df = df.drop_duplicates()

    df.to_csv("data/silver/payments_clean.csv", index=False)

    print("✅ payments_clean.csv generated")