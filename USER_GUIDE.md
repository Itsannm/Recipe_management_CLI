# Recipe Manager CLI - User and Installation Guide

## Overview
Welcome to the Recipe Manager CLI, a command-line tool designed to simplify recipe management. 

## Features
The Recipe Manager CLI offers the following features:

- **Add Recipe**: Seamlessly add new recipes to your collection, complete with titles, instructions, and ingredients.
- **List Recipes**: Quickly retrieve a comprehensive list of all your recipes.
- **Delete Recipe**: Effortlessly remove a recipe from your collection by specifying its unique ID.
- **Edit Recipe**: Modify existing recipes with ease, updating titles, instructions, or ingredients as needed.
- **Search Recipes**: Locate recipes effortlessly by searching for specific titles, simplifying the retrieval process.
- **View Recipe**: Access detailed information about a specific recipe, including its title, instructions, and ingredients.

## Installation
Follow these steps to install the Recipe Manager CLI:

1. Clone this project repository to your local machine.
2. Navigate to the project directory.
3. Execute the following command to install the necessary dependencies:

```bash
pipenv install
pipenv shell
cd recipe_manager
```

## Usage
Here are some common usage examples to get you started:

- To list all recipes, use the following command:

```bash
python3 -m list-recipes
```

- To add a new recipe, simply run:

```bash
python3 -m cli add-recipe
```

- Deleting a recipe is straightforward; use:

```bash
python3 -m cli delete-recipe
```

- Editing an existing recipe is as simple as:

```bash
python3 -m cli edit-recipe
```

- To search for recipes by title, execute:

```bash
python3 -m cli search-recipes
```

- Detailed information about a specific recipe can be obtained with:

```bash
python3 -m cli view-recipe
```

## Documentation
For in-depth guidance on using the Recipe Manager CLI, please refer to the comprehensive documentation available in the `docs` directory.

## Conclusion
The Recipe Manager CLI simplifies recipe management and retrieval, offering a straightforward and efficient solution for culinary enthusiasts and home cooks alike. Give it a try and elevate your cooking experience!

For any questions or feedback, please feel free to reach out. Thank you for choosing the Recipe Manager CLI for your recipe organization needs.