import pandas as pd

def run():
    print("📊 Generating revenue by country...")

    # -----------------------------------------
    # 1. LOAD DATA
    # -----------------------------------------
    orders = pd.read_csv("data/silver/orders_clean.csv")
    customers = pd.read_csv("data/silver/customers_clean.csv")
    products = pd.read_csv("data/silver/products_clean.csv")

    # -----------------------------------------
    # 2. JOIN DATA
    # -----------------------------------------
    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(products, on="product_id", how="left")

    # -----------------------------------------
    # 3. BUSINESS METRICS
    # -----------------------------------------
    df["total"] = df["quantity"] * df["price"]

    result = df.groupby("country").agg(
        total_revenue=("total", "sum"),
        total_orders=("order_id", "count")
    ).reset_index()

    # -----------------------------------------
    # 4. SAVE GOLD DATA
    # -----------------------------------------
    result.to_csv("data/gold/revenue_by_country.csv", index=False)

    print("✅ revenue_by_country.csv generado")