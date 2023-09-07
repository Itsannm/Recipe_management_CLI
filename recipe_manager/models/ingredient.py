# my_app/my_app/models/ingredient.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

# Define the Ingredient model
class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    recipes = relationship("Recipe", secondary="recipe_ingredients", back_populates="ingredients")
