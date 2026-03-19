import pandas as pd

print("🥉 Bronze Layer")

datasets = [
    "customers",
    "products",
    "orders",
    "payments"
]

for ds in datasets:
    path = f"data/bronze/{ds}.csv"
    df = pd.read_csv(path)

    print(f"Loaded {ds}: {len(df)} rows")

print("✅ Bronze layer completed")