# recipe_manager/cli.py

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database connection string (SQLite in this example)
DATABASE_URL = 'sqlite:///recipe_manager.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.command()
def list_recipes():
    """List all recipes."""
    # Create a database session
    session = Session()

    # Implement the logic to fetch and display recipes here

    # Remember to close the session
    session.close()

if __name__ == '__main__':
    list_recipes()
