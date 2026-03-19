import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker()

Path("data/bronze").mkdir(parents=True, exist_ok=True)

# -----------------------------
# CUSTOMERS
# -----------------------------

customers = []

for i in range(1, 51):
    customers.append({
        "customer_id": i,
        "name": fake.name() if random.random() > 0.1 else None,
        "email": fake.email() if random.random() > 0.2 else "invalid_email",
        "country": random.choice(["Peru", "USA", "Spain", "Mexico", None]),
        "signup_date": fake.date_between(start_date="-3y", end_date="today")
    })

# duplicado intencional
customers.append(customers[5])

pd.DataFrame(customers).to_csv(
    "data/bronze/customers.csv", index=False
)

# -----------------------------
# PRODUCTS
# -----------------------------

products = []

categories = ["Electronics", "Books", "Clothing", "Home", None]

for i in range(1, 51):

    price = round(random.uniform(5, 500), 2)

    # error intencional
    if random.random() < 0.1:
        price = -price

    products.append({
        "product_id": i,
        "name": fake.word(),
        "category": random.choice(categories),
        "price": price
    })

products.append(products[10])

pd.DataFrame(products).to_csv(
    "data/bronze/products.csv", index=False
)

# -----------------------------
# ORDERS
# -----------------------------

orders = []

for i in range(1, 51):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 60),  # FK rota
        "product_id": random.randint(1, 60),   # FK rota
        "quantity": random.randint(1, 5),
        "order_date": fake.date_between(start_date="-2y", end_date="today")
    })

orders.append(orders[7])

pd.DataFrame(orders).to_csv(
    "data/bronze/orders.csv", index=False
)

# -----------------------------
# PAYMENTS
# -----------------------------

payments = []

methods = ["credit_card", "paypal", "bank_transfer", None]

for i in range(1, 51):

    amount = round(random.uniform(10, 1000), 2)

    if random.random() < 0.1:
        amount = -amount

    payments.append({
        "payment_id": i,
        "order_id": random.randint(1, 60),  # FK rota
        "payment_method": random.choice(methods),
        "amount": amount,
        "payment_date": fake.date_between(start_date="-2y", end_date="today")
    })

payments.append(payments[3])

pd.DataFrame(payments).to_csv(
    "data/bronze/payments.csv", index=False
)

print("✅ CSV datasets generated in data/bronze/")