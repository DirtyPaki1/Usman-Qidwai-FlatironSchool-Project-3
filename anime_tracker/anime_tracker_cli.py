import os
from anime_tracker_db import Season, AnimeSeries, get_session, close_connection, initialize_database
import click

def create_season(session, name, year):
    season = Season(name=name, year=year)
    session.add(season)
    session.commit()
    print(f"Created season: {season}")

def delete_season(session, season_id):
    season = session.query(Season).filter_by(id=season_id).first()
    if season:
        session.delete(season)
        session.commit()
        print(f"Deleted season: {season}")
    else:
        print("Season not found.")

def display_all_seasons(session):
    seasons = session.query(Season).all()
    for season in seasons:
        print(season)

def view_season_anime_series(session, season_id):
    season = session.query(Season).filter_by(id=season_id).first()
    if season:
        anime_series = season.anime_series
        print(f"Anime Series for season '{season.name} ({season.year}'):")
        for series in anime_series:
            print(series.title)
    else:
        print("Season not found.")

def find_season_by_name_year(session, name, year):
    season = session.query(Season).filter(Season.name.like(f"%{name}%"), Season.year == year).first()
    if season:
        print(f"Found season: {season}")
    else:
        print("Season not found.")

def create_anime_series(session, title, genre, episodes, rating, season_id):
    anime_series = AnimeSeries(title=title, genre=genre, episodes=episodes, rating=rating, season_id=season_id)
    session.add(anime_series)
    session.commit()
    print(f"Added anime series: {anime_series}")

def delete_anime_series(session, anime_series_id):
    anime_series = session.query(AnimeSeries).filter_by(id=anime_series_id).first()
    if anime_series:
        session.delete(anime_series)
        session.commit()
        print(f"Deleted anime series: {anime_series}")
    else:
        print("Anime series not found.")

def display_all_anime_series(session):
    anime_series = session.query(AnimeSeries).all()
    for series in anime_series:
        print(series)

def find_anime_series_by_title(session, title):
    anime_series = session.query(AnimeSeries).filter(AnimeSeries.title.like(f"%{title}%")).first()
    if anime_series:
        print(f"Found anime series: {anime_series}")
    else:
        print("Anime series not found.")

def main():
    # Initialize the database
    initialize_database()

    session = get_session()

    while True:
        print("\nAnime Tracker Menu:")
        print("1. Add Season")
        print("2. Delete Season")
        print("3. Display All Seasons")
        print("4. View Anime Series for Season")
        print("5. Find Season by Name and Year")
        print("6. Add Anime Series")
        print("7. Delete Anime Series")
        print("8. Display All Anime Series")
        print("9. Find Anime Series by Title")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            name = input("Enter season name: ")
            year = int(input("Enter season year: "))
            create_season(session, name, year)
        elif choice == '2':
            season_id = int(input("Enter season ID to delete: "))
            delete_season(session, season_id)
        elif choice == '3':
            display_all_seasons(session)
        elif choice == '4':
            season_id = int(input("Enter season ID to view anime series: "))
            view_season_anime_series(session, season_id)
        elif choice == '5':
            name = input("Enter partial season name to search: ")
            year = int(input("Enter season year: "))
            find_season_by_name_year(session, name, year)
        elif choice == '6':
            title = input("Enter anime series title: ")
            genre = input("Enter genre: ")
            episodes = int(input("Enter number of episodes: "))
            rating = float(input("Enter rating (out of 10): "))
            season_id = int(input("Enter season ID: "))
            create_anime_series(session, title, genre, episodes, rating, season_id)
        elif choice == '7':
            anime_series_id = int(input("Enter anime series ID to delete: "))
            delete_anime_series(session, anime_series_id)
        elif choice == '8':
            display_all_anime_series(session)
        elif choice == '9':
            title = input("Enter partial anime series title to search: ")
            find_anime_series_by_title(session, title)
        elif choice == '10':
            print("Exiting...")
            close_connection(session)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
