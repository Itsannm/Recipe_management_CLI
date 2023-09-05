# recipe_manager/cli.py

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import your SQLAlchemy models here
from recipe_manager.models import User, Recipe, Ingredient

# Define your DATABASE_URL here
DATABASE_URL = 'sqlite:///recipe_manager.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

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

@click.command()
@click.option('--title', prompt='Title of the recipe', help='Title of the recipe')
@click.option('--instructions', prompt='Recipe instructions', help='Instructions for the recipe')
@click.option('--ingredients', prompt='Recipe ingredients (comma-separated)', help='Ingredients for the recipe')
def add_recipe(title, instructions, ingredients):
    """Add a new recipe."""
    session = Session()
    
    # Split ingredients into a list
    ingredient_list = [name.strip() for name in ingredients.split(',')]
    
    # Create a new recipe and add it to the database
    new_recipe = Recipe(title=title, instructions=instructions)
    
    # Fetch or create ingredients and add them to the recipe
    for ingredient_name in ingredient_list:
        ingredient = session.query(Ingredient).filter_by(name=ingredient_name).first()
        if not ingredient:
            ingredient = Ingredient(name=ingredient_name)
        new_recipe.ingredients.append(ingredient)
    
    session.add(new_recipe)
    session.commit()
    session.close()

@click.command()
@click.option('--recipe_id', prompt='Recipe ID to delete', help='ID of the recipe to delete')
def delete_recipe(recipe_id):
    """Delete a recipe by its ID."""
    session = Session()
    
    # Find the recipe by ID and delete it
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    
    if recipe:
        session.delete(recipe)
        session.commit()
        click.echo(f"Recipe with ID {recipe_id} deleted.")
    else:
        click.echo(f"No recipe found with ID {recipe_id}.")
    
    session.close()

if __name__ == '__main__':
    # Add the commands to the CLI interface
    add_recipe()
    list_recipes()
    delete_recipe()
