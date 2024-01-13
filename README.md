# Phase-3-Project
# Python Phase 3 Project - CLI Application

Project Name: CLI Application

- A command-line interface (CLI) application for managing user orders and products in a database using Python, SQLAlchemy, and Alembic.

## Tools Used

- Python: The programming language used for developing the CLI application.
- SQLAlchemy: A Python SQL toolkit and Object-Relational Mapping (ORM) library for managing the database.
- Alembic: A database migration tool for managing schema changes over time.
- Click: A Python library for creating command-line interfaces.
- Pipenv: A tool for managing Python virtual environments and project dependencies.
- SQLite: A lightweight, file-based database engine used in the project.

## Environment Setup

- Instructions for setting up the virtual environment and installing dependencies using Pipenv.

## SQL Database

- Utilizes SQLAlchemy to create and manage three related tables in the database: User, Order, and Product.
- Database migrations are handled using Alembic with separate scripts for creating the database and tables.
- Python logic in the CLI application handles data querying and manipulation using SQLAlchemy.

## Data Structures and Algorithms (DSA)

- Utilizes Python data structures (lists, dictionaries, tuples) to manage data within the CLI.
- Includes the implementation of a relevant algorithm from a Data Structures and Algorithms (DSA) module.

## CLI Best Practices

- Separates scripted elements from object-oriented code.
- Validates user input to ensure data integrity.
- Provides detailed prompts and messages to guide the user throughout the execution of the CLI.
- Minimizes project-specific code by using external libraries such as SQLAlchemy, Alembic, and Click.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/iamMwirigi/Phase-3-Project.git
## Configuration
- Database configuration is defined in app/database.py.
- Database URL can be configured via environment variables or command-line arguments.

## Testing
- To run tests, use a testing framework like pytest and create test cases for your CLI commands and database operations.

## License
- This project is licensed under the MIT License.