# Recipe Manager CLI

Recipe Manager CLI is a command-line application that allows users to manage and organize their recipes. This application uses Python and various libraries, including SQLAlchemy and Click, to provide a seamless recipe management experience.

## Features

### Current Features

1. **Recipe Management**:
   - Add, edit, search and delete recipes.
   - Each recipe includes a title, ingredients and instructions.
   


3. **Database Schema**:
   - Utilizes SQLAlchemy ORM to create a database schema with three related tables: Users, Recipes, and Ingredients.
   - Establishes one-to-many relationships between Users and Recipes and many-to-many relationships between Recipes and Ingredients.

4. **CLI Commands**:
   - Implements CLI commands using Click to manage recipes, including add, edit, delete, list, search, and view.

5. **Environment Management**:
   - Sets up a well-maintained virtual environment using Pipenv to manage project-specific parameters and dependencies.

6. **Package Structure**:
   - Organizes the project with a proper package structure, separating Python objects, SQLAlchemy objects, and the CLI script into different modules.

7. **External Libraries**:
   - Imports and uses external libraries for user authentication, searching algorithms, and CLI interface.

### Future Features

While the current version of Recipe Manager CLI offers powerful recipe management capabilities, there are several exciting features that can be added in the future:

1. **Meal Planning**:
   - Allow users to plan meals by selecting recipes for specific dates, creating shopping lists, and tracking nutritional information.

2. **Recipe Sharing**:
   - Enable users to share their favorite recipes with others in the community.

3. **User Profiles**:
   - Create user profiles with customizable avatars and personal information.

4. **Recipe Ratings and Reviews**:
   - Implement a rating and review system for recipes, allowing users to provide feedback and recommendations.

5. **Integration with Recipe APIs**:
   - Connect to external recipe databases or APIs to import recipes from popular cooking websites.

6. **Recipe Categories**:
   - Categorize recipes into different types, such as appetizers, main courses, desserts, etc., for easier organization.

7. **Enhanced Search**:
   - Improve the ingredient-based search algorithm to provide more accurate and relevant recipe suggestions.

8. **Ingredient-Based Search**:
   - Implement an algorithm to search for recipes based on available ingredients.
   - Users can input ingredients they have, and the CLI will suggest recipes they can make.

9.**Mobile App**:
   - Develop a mobile application version of Recipe Manager CLI for users on the go.


## Usage

To install, run Recipe Manager CLI and for detailed usage instructions, refer to the [User Guide](USER_GUIDE.md).

## Contributing
Contributions from the open-source community are welcomed! 

## License

Recipe Manager CLI is licensed under the [MIT License](LICENSE).

## Author

- Ann Mwanzia

Happy cooking and recipe management!
