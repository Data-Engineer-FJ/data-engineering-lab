import pandas as pd

def run():
    print("🧹 Cleaning customers...")

    # -----------------------------------------
    # 1. LOAD DATA (Bronze)
    # -----------------------------------------
    df = pd.read_csv("data/bronze/customers.csv")

    # Normalizar nombres de columnas (evita errores de schema)
    df.columns = [col.lower().strip() for col in df.columns]

    # -----------------------------------------
    # 2. DATA CLEANING
    # -----------------------------------------

    # Eliminar registros sin nombre
    df = df[df["name"].notna() & (df["name"] != "")]

    # Eliminar emails inválidos
    df = df[df["email"].str.contains("@", na=False)]

    # Manejo de valores faltantes en country
    df["country"] = df["country"].replace("", "UNKNOWN").fillna("UNKNOWN")

    # Estandarizar texto (importante para joins y agregaciones)
    df["country"] = df["country"].str.upper()

    # -----------------------------------------
    # 3. SAVE DATA (Silver)
    # -----------------------------------------
    df.to_csv("data/silver/customers_clean.csv", index=False)

    print("✅ customers_clean.csv generado")