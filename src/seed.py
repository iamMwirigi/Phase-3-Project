from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.models import User, Order, Product
from src.database import init_db

def seed_data():
    # Initialize the database session
    db = init_db()

    # Sample users
    users_data = [
        {"username": "john_doe"},
        {"username": "alice_smith"},
        # Add more users as needed
    ]

    # Sample products
    products_data = [
        {"name": "Laptop"},
        {"name": "Headphones"},
        # Add more products as needed
    ]

    # Sample orders
    orders_data = [
        {"username": "john_doe", "product_name": "Laptop"},
        {"username": "alice_smith", "product_name": "Headphones"},
        # Add more orders as needed
    ]

    # Insert users into the database
    for user_info in users_data:
        user = User(**user_info)
        db.add(user)

    # Insert products into the database
    for product_info in products_data:
        product = Product(**product_info)
        db.add(product)

    # Commit changes to the database
    db.commit()

    # Retrieve user and product instances for creating orders
    users = {user.username: user for user in db.query(User).all()}
    products = {product.name: product for product in db.query(Product).all()}

    # Insert orders into the database
    for order_info in orders_data:
        username = order_info["username"]
        product_name = order_info["product_name"]

        user = users.get(username)
        product = products.get(product_name)

        if user and product:
            order = Order(user=user, product=product)
            db.add(order)

    # Commit changes to the database
    db.commit()

if __name__ == '__main__':
    seed_data()
    print("Database seeded successfully.")
