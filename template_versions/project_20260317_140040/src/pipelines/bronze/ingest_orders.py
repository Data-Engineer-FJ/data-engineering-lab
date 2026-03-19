import pandas as pd

def run():
    print("📥 Ingesting orders...")

    df = pd.read_csv("data/bronze/orders.csv")

    print(f"✅ orders loaded: {len(df)} rows")

    return df