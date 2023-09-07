# my_app/my_app/models/recipe_ingredients.py

from sqlalchemy import Column, Integer, ForeignKey, Table
from models.base import Base

# Define the association table
recipe_ingredients = Table(
    'recipe_ingredients',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)
