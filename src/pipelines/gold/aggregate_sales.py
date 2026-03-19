import pandas as pd

def run():
    print("📊 Generating sales summary...")

    # -----------------------------------------
    # 1. LOAD CLEAN DATA
    # -----------------------------------------
    orders = pd.read_csv("data/silver/orders_clean.csv")
    products = pd.read_csv("data/silver/products_clean.csv")

    # -----------------------------------------
    # 2. JOIN DATASETS
    # -----------------------------------------
    df = orders.merge(products, on="product_id", how="left")

    # -----------------------------------------
    # 3. BUSINESS LOGIC
    # -----------------------------------------
    df["total"] = df["quantity"] * df["price"]

    # Agregación
    result = df.groupby("product_name").agg(
        total_sales=("total", "sum"),
        total_orders=("order_id", "count")
    ).reset_index()

    # -----------------------------------------
    # 4. SAVE GOLD DATA
    # -----------------------------------------
    result.to_csv("data/gold/sales_summary.csv", index=False)

    print("✅ sales_summary.csv generado")