import pandas as pd

def run():
    print("🧹 Cleaning payments...")

    # -----------------------------------------
    # 1. LOAD DATA
    # -----------------------------------------
    df = pd.read_csv("data/bronze/payments.csv")

    df.columns = [col.lower().strip() for col in df.columns]

    # -----------------------------------------
    # 2. DATA CLEANING
    # -----------------------------------------

    # Validar montos
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Eliminar montos negativos o inválidos
    df = df[df["amount"] > 0]

    # Limpiar método de pago
    df["payment_method"] = df["payment_method"].replace("", "UNKNOWN")
    df["payment_method"] = df["payment_method"].fillna("UNKNOWN")

    # Estandarizar texto
    df["payment_method"] = df["payment_method"].str.upper()

    # -----------------------------------------
    # 3. SAVE DATA
    # -----------------------------------------
    df.to_csv("data/silver/payments_clean.csv", index=False)

    print("✅ payments_clean.csv generado")