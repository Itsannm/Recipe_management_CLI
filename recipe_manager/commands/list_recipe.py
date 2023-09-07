# my_app/commands/list_recipes.py

import click
from sqlalchemy.orm import sessionmaker
from models.recipe import Recipe 
from cli import Session

@click.command()
def list_recipes():
    """List all recipes."""
    session = Session()
    
    # Fetch all recipes from the database
    recipes = session.query(Recipe).all()
    
    if recipes:
        click.echo("Recipes:")
        for recipe in recipes:
            click.echo(f"- {recipe.title}")
    else:
        click.echo("No recipes found.")
    
    session.close()
