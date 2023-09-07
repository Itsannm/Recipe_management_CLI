# seeds.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from recipe_manager.models import User, Recipe, Ingredient  # Import your models from recipe_manager

# Create a SQLite database
engine = create_engine('sqlite:///recipe_manager.db')

# Create tables in the database
from recipe_manager.models import Base, recipe_ingredients  # Import Base and the association table
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Sample data for ingredients
ingredient1 = Ingredient(name="pasta")
ingredient2 = Ingredient(name="egg")
ingredient3 = Ingredient(name="cheese")
ingredient4 = Ingredient(name="tomato")
ingredient5 = Ingredient(name="bread")
ingredient6 = Ingredient(name="lettuce")

# Sample data for users (if your application has user authentication)
user1 = User(username="user1", password="password1")
user2 = User(username="user2", password="password2")

# Sample data for recipes
recipe1 = Recipe(
    title="Pasta Carbonara",
    instructions="Cook pasta, mix with egg and cheese.",
    user=user1  # Assign a user to the recipe if applicable
)
recipe2 = Recipe(
    title="Caprese Salad",
    instructions="Slice tomatoes and mozzarella, add basil leaves.",
    user=user2  # Assign a user to the recipe if applicable
)
recipe3 = Recipe(
    title="Egg Salad Sandwich",
    instructions="Make a sandwich with egg salad and lettuce.",
    user=user1  # Assign a user to the recipe if applicable
)

# Associate ingredients with recipes using the many-to-many relationship
recipe_ingredients_data = [
    {'recipe': recipe1, 'ingredient': ingredient1},
    {'recipe': recipe1, 'ingredient': ingredient2},
    {'recipe': recipe1, 'ingredient': ingredient3},
    {'recipe': recipe2, 'ingredient': ingredient4},
    {'recipe': recipe2, 'ingredient': ingredient3},
    {'recipe': recipe3, 'ingredient': ingredient2},
    {'recipe': recipe3, 'ingredient': ingredient5},
    {'recipe': recipe3, 'ingredient': ingredient6},
]

for data in recipe_ingredients_data:
    data['recipe'].ingredients.append(data['ingredient'])

# Add data to the session and commit it to the database
session.add_all([
    ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6,
    user1, user2,
    recipe1, recipe2, recipe3
])
session.commit()

# Close the session
session.close()
