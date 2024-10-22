Recipe Box Application
A simple Python-based recipe management tool designed to help users organize and access their favorite recipes easily.

What is it?
The Recipe Box Application is a command-line program that allows users to store, manage, and retrieve recipes and ingredients. It's designed to be user-friendly and easy to use, perfect for home cooks who want to keep track of their favorite dishes and essential pantry items.

Key Features
Add new recipes with details like title, description, cuisine, difficulty, and cooking time
Delete existing recipes from the database
View all recipes stored in the application
Add new ingredients with quantity and unit information
Delete ingredients from the database
View all ingredients added to the system
Search for recipes by partial title
Search for ingredients by partial name
Save all data to a JSON file for persistence across sessions
How it Works
Starting the Application When you run the Recipe Box Application, it loads data from a JSON file (if available) or creates a new empty database.
Main Menu The application presents a simple text-based menu with options to perform various actions.
Adding Recipes
Users can add new recipes by entering the requested details.
The application stores this information in memory and saves it to the JSON file.
Managing Ingredients
Users can add new ingredients with quantity and unit information.
They can also view all ingredients or search for specific ones.
Searching Recipes and Ingredients
The application supports partial searches for both recipes and ingredients.
This means users can quickly find what they're looking for even if they remember only part of the name.
Saving Data
At any point, users can save all their data to the JSON file.
This ensures that their work is preserved even if they close the application unexpectedly.
Closing the Application
Users can exit the application at any time, and their data will be saved automatically.
Benefits
Easy to use: No complex interfaces or steep learning curves.
Portable: Runs on most devices with Python installed.
Flexible: Allows users to customize their own recipe collection.
Persistent: Keeps track of your recipes and ingredients between sessions.