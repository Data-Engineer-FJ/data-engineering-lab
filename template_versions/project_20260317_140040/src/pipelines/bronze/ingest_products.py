import pandas as pd

def run():
    print("📥 Ingesting products...")

    df = pd.read_csv("data/bronze/products.csv")

    print(f"✅ products loaded: {len(df)} rows")

    return df