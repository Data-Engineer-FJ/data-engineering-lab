import pandas as pd

def run():
    print("🌎 Generating revenue_by_country...")

    customers = pd.read_csv("data/silver/customers_clean.csv")
    orders = pd.read_csv("data/silver/orders_clean.csv")
    payments = pd.read_csv("data/silver/payments_clean.csv")

    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(payments, on="order_id", how="left")

    result = df.groupby("country").agg(
        total_revenue=("amount", "sum"),
        total_orders=("order_id", "count")
    ).reset_index()

    result.to_csv("data/gold/revenue_by_country.csv", index=False)

    print("✅ revenue_by_country.csv generated")