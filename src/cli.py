import click
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.models import User, Order, Product
from src.database import init_db
from models import User, Order, Product
cd 

@click.group()
def cli():
    pass

@cli.command()
@click.option('--username', prompt='Enter the username', help='Username of the user to add')
def add_user(username):
    # Initialize the database session
    db = init_db()

    # Check if the user already exists
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        print(f"User with username '{username}' already exists.")
    else:
        # Create a new user
        new_user = User(username=username)
        db.add(new_user)
        db.commit()
        print(f"User '{username}' added successfully.")

@cli.command()
@click.option('--product_name', prompt='Enter the product name', help='Name of the product to add')
def add_product(product_name):
    # Initialize the database session
    db = init_db()

    # Check if the product already exists
    existing_product = db.query(Product).filter(Product.name == product_name).first()
    if existing_product:
        print(f"Product with name '{product_name}' already exists.")
    else:
        # Create a new product
        new_product = Product(name=product_name)
        db.add(new_product)
        db.commit()
        print(f"Product '{product_name}' added successfully.")

@cli.command()
@click.option('--username', prompt='Enter the username', help='Username of the user placing the order')
@click.option('--product_name', prompt='Enter the product name', help='Name of the product to order')
def create_order(username, product_name):
    # Initialize the database session
    db = init_db()

    # Retrieve user and product by their names
    user = db.query(User).filter(User.username == username).first()
    product = db.query(Product).filter(Product.name == product_name).first()

    if user and product:
        # Create an order for the user
        order = Order(user=user, product=product)
        db.add(order)
        db.commit()
        print(f"Order created for {username}: {product_name}")
    else:
        print("User or product not found.")

if __name__ == '__main__':
    cli()
