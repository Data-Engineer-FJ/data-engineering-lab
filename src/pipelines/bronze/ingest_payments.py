import pandas as pd

def run():
    print("📥 Ingesting payments...")

    df = pd.read_csv("data/bronze/payments.csv")

    print(f"✅ payments loaded: {len(df)} rows")

    return df