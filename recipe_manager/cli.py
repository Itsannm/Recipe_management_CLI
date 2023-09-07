# my_app/my_app/cli.py

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Recipe, Ingredient
from commands.list_recipe import list_recipes
from commands.add_recipe import add_recipe
from commands.delete_recipe import delete_recipe
from commands.edit_recipe import edit_recipe
from commands.search_recipe import search_recipes
from commands.view_recipe import view_recipe

# Define your DATABASE_URL here
DATABASE_URL = 'sqlite:///recipe_manager.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Recipe Manager CLI"""

# Add command functions as subcommands
cli.add_command(list_recipes)
cli.add_command(add_recipe)
cli.add_command(delete_recipe)
cli.add_command(edit_recipe)
cli.add_command(search_recipes)
cli.add_command(view_recipe)

if __name__ == '__main__':
    cli()
