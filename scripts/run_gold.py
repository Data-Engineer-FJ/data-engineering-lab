import sys
import os

# 👇 Esto arregla el import de src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.pipelines.gold.aggregate_sales import run as sales
from src.pipelines.gold.revenue_by_country import run as country


def main():
    print("🥇 Gold Layer")

    sales()
    country()

    print("✅ Gold completed")


if __name__ == "__main__":
    main()