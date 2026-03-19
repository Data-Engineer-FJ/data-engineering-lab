import pandas as pd

def run():
    print("🧹 Cleaning products...")

    # -----------------------------------------
    # 1. LOAD DATA
    # -----------------------------------------
    df = pd.read_csv("data/bronze/products.csv")

    df.columns = [col.lower().strip() for col in df.columns]

    # Estandarizar nombre de columna
    df = df.rename(columns={"name": "product_name"})

    # -----------------------------------------
    # 2. DATA CLEANING
    # -----------------------------------------

    # Eliminar productos sin nombre o precio
    df = df.dropna(subset=["product_name", "price"])

    # Convertir precio a numérico
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Filtrar valores inválidos
    df = df[df["price"] > 0]

    # Limpiar texto
    df["product_name"] = df["product_name"].str.strip()

    # -----------------------------------------
    # 3. SAVE DATA
    # -----------------------------------------
    df.to_csv("data/silver/products_clean.csv", index=False)

    print("✅ products_clean.csv generado")