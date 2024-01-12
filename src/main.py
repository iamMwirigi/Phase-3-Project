# Import necessary modules
import click
from src.database import init_db
from src.models import User, Order, Product
from sqlalchemy.orm import Session

@click.group()
def cli():
    pass

@cli.command()
@click.argument('username')
@click.argument('product_name')
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

@cli.command()
@click.argument('username')
def list_orders(username):
    # Initialize the database session
    db = init_db()

    # Retrieve user by username
    user = db.query(User).filter(User.username == username).first()

    if user:
        # List orders for the user
        orders = db.query(Order).filter(Order.user_id == user.id).all()
        if orders:
            for order in orders:
                print(f"Order ID: {order.id}, Product: {order.product.name}")
        else:
            print(f"No orders found for {username}.")
    else:
        print("User not found.")

if __name__ == '__main__':
    cli()
