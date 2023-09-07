# my_app/commands/add_recipe.py

import click
from sqlalchemy.orm import sessionmaker
from my_app.models import Recipe, Ingredient
from my_app.cli import Session

@click.command()
@click.option('--title', prompt='Title of the recipe', help='Title of the recipe')
@click.option('--instructions', prompt='Recipe instructions', help='Instructions for the recipe')
@click.option('--ingredients', prompt='Recipe ingredients (comma-separated)', help='Ingredients for the recipe')
def add_recipe(title, instructions, ingredients):
    """Add a new recipe."""
    session = Session()
    
    # Split ingredients into a list
    ingredient_list = [name.strip() for name in ingredients.split(',')]
    
    if not title or not instructions or not ingredient_list:
        click.echo("Invalid input. Please provide a title, instructions, and ingredients.")
        session.close()
        return
    
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
    
    click.echo(f"Recipe '{title}' added successfully!")
