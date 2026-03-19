import pandas as pd

def run():
    print("🧹 Cleaning orders...")

    # -----------------------------------------
    # 1. LOAD DATA
    # -----------------------------------------
    df = pd.read_csv("data/bronze/orders.csv")

    df.columns = [col.lower().strip() for col in df.columns]

    # -----------------------------------------
    # 2. DATA CLEANING
    # -----------------------------------------

    # Eliminar registros sin claves
    df = df.dropna(subset=["customer_id", "product_id"])

    # Validar cantidades
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df = df[df["quantity"] > 0]

    # -----------------------------------------
    # 3. SAVE DATA
    # -----------------------------------------
    df.to_csv("data/silver/orders_clean.csv", index=False)

    print("✅ orders_clean.csv generado")