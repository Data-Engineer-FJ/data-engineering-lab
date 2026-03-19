import pandas as pd

def run():
    print("📥 Ingesting customers...")

    df = pd.read_csv("data/bronze/customers.csv")

    print(f"✅ customers loaded: {len(df)} rows")

    return df