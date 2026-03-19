import os

BASE_PATH = "src/pipelines"

STRUCTURE = {
    "bronze": {
        "ingest_customers.py": """
import pandas as pd

def run():
    print("📥 Ingesting customers...")
    df = pd.read_csv("data/bronze/customers.csv")
    print(f"Loaded {len(df)} rows")
    return df
""",
        "ingest_products.py": """
import pandas as pd

def run():
    print("📥 Ingesting products...")
    df = pd.read_csv("data/bronze/products.csv")
    print(f"Loaded {len(df)} rows")
    return df
""",
    },

    "silver": {
        "transform_customers.py": """
import pandas as pd

def run():
    print("🧹 Cleaning customers...")
    df = pd.read_csv("data/bronze/customers.csv")
    df = df.drop_duplicates()
    df["email"] = df["email"].fillna("unknown")
    df.to_csv("data/silver/customers_clean.csv", index=False)
""",

        "transform_products.py": """
import pandas as pd

def run():
    print("🧹 Cleaning products...")
    df = pd.read_csv("data/bronze/products.csv")
    df = df.drop_duplicates()
    df = df[df["price"] > 0]
    df.to_csv("data/silver/products_clean.csv", index=False)
""",

        "transform_orders.py": """
import pandas as pd

def run():
    print("🧹 Cleaning orders...")
    df = pd.read_csv("data/bronze/orders.csv")
    df = df.drop_duplicates()
    df.to_csv("data/silver/orders_clean.csv", index=False)
""",

        "transform_payments.py": """
import pandas as pd

def run():
    print("🧹 Cleaning payments...")
    df = pd.read_csv("data/bronze/payments.csv")
    df = df.drop_duplicates()
    df.to_csv("data/silver/payments_clean.csv", index=False)
"""
    },

    "gold": {
        "aggregate_sales.py": """
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

    df.to_csv("data/gold/sales_summary.csv", index=False)
""",

        "revenue_by_country.py": """
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
"""
    }
}


def create_structure():
    for layer, files in STRUCTURE.items():

        layer_path = os.path.join(BASE_PATH, layer)
        os.makedirs(layer_path, exist_ok=True)

        # __init__.py
        init_file = os.path.join(layer_path, "__init__.py")
        open(init_file, "w").close()

        for filename, content in files.items():

            file_path = os.path.join(layer_path, filename)

            with open(file_path, "w") as f:
                f.write(content.strip())

            print(f"✅ Created {file_path}")


if __name__ == "__main__":
    print("🚀 Generating real pipeline structure...\n")
    create_structure()
    print("\n🎉 Pipelines ready to run!")