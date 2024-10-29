


Movie Actor Database CLI Application

Project Overview

The Movie Actor Database CLI Application is a command-line tool for managing a simple database of movies and actors. It lets users create, view, and delete entries for movies and actors, as well as associate actors with movies they’ve starred in. Designed with ease of use in mind, this CLI is built entirely with Python, using SQLite for the database and without any external ORM libraries.

Features

Add Movies and Actors: Input movie titles, release years, actor names, and ages, and save them in the database.
View All Movies and Actors: Display all movies and actors with options to list related information.
Search and Delete: Find movies or actors by name and remove entries if needed.
View Relationships: List all actors in a selected movie, supporting easy exploration of movie casts.
Steps
Clone the Repository:

git clone https://github.com/yourusername/movie_actor_project.git
cd movie_actor_project

Install Dependencies:

pipenv install

Activate the Virtual Environment:
pipenv shell

Initialize the Database: Run this command to create the database and tables:

python lib/initialize_db.py

Check Database Tables (Optional): To verify the tables were created, run:
python lib/check_tables.py

Run the CLI Application: Start the application by entering:
python -m lib.cli


Using the CLI

Once the CLI is running, you’ll see options to manage your movie and actor entries:

Add a New Movie or Actor: Follow prompts to input details for movies and actors.
View All Entries: List all movies and actors saved in the database.
Search by Name: Look up movies or actors by name.
Delete Entries: Remove a selected movie or actor.
View Actors in a Movie: See all actors associated with a specific movie.






