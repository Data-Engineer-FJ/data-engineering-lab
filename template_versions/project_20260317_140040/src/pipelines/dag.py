DAG = {
    "silver": {
        "transform_customers": [],
        "transform_products": [],
        "transform_orders": [],
        "transform_payments": [],
    },
    "gold": {
        "aggregate_sales": ["transform_orders", "transform_products"],
        "revenue_by_country": ["transform_payments", "transform_customers"],
    }
}