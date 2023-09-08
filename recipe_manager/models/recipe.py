# my_app/my_app/models/recipe.py

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base import Base

# Define the Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    instructions = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="recipes")

    ingredients = relationship("Ingredient", secondary="recipe_ingredients", back_populates="recipes")
