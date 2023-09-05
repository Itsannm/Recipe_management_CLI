# recipe_manager/cli.py

import click

@click.command()
@click.option('--title', prompt='Title of the recipe', help='Title of the recipe')
@click.option('--instructions', prompt='Recipe instructions', help='Instructions for the recipe')
def add_recipe(title, instructions):
    """Add a new recipe."""
    # Implement the logic to add a recipe to the database here
    pass

if __name__ == '__main__':
    add_recipe()
