import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.pipelines.silver.transform_customers import run as customers
from src.pipelines.silver.transform_products import run as products
from src.pipelines.silver.transform_orders import run as orders
from src.pipelines.silver.transform_payments import run as payments


def main():
    print("🥈 Silver Layer")

    customers()
    products()
    orders()
    payments()

    print("✅ Silver completed")


if __name__ == "__main__":
    main()