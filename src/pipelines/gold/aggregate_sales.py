import pandas as pd

def run():
    print("📊 Generating sales_summary...")

    orders = pd.read_csv("data/silver/orders_clean.csv")
    payments = pd.read_csv("data/silver/payments_clean.csv")

    df = orders.merge(payments, on="order_id", how="left")

    summary = df.groupby("payment_method").agg(
        total_orders=("order_id", "count"),
        total_revenue=("amount", "sum")
    ).reset_index()

    summary.to_csv("data/gold/sales_summary.csv", index=False)

    print("✅ sales_summary.csv generated")