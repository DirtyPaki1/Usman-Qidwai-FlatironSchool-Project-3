import click
from anime_tracker_db import Season, AnimeSeries, get_session
import time

@click.group()
def cli():
    """Anime Tracker CLI"""
    pass

@cli.command('seasons')
def list_seasons():
    """List all seasons"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            print("No seasons found.")
            return
        
        print("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            print(f"{i}. {season.name} ({season.year})")

@cli.command('add_season')
def add_season():
    """Add a new season"""
    name = input("Enter season name: ")
    year = int(input("Enter year: "))
    
    with get_session() as session:
        existing_season = session.query(Season).filter_by(name=name, year=year).first()
        if existing_season:
            print("Season already exists.")
            return
        
        season = Season.create(session, name, year)
        print(f"Added '{name}' ({year})")

@cli.command('delete_season')
def delete_season():
    """Delete a season"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            print("No seasons found.")
            return
        
        print("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            print(f"{i}. {season.name} ({season.year})")
        
        while True:
            try:
                choice = int(input("\nEnter the number of the season to delete, or 0 to cancel: "))
                if choice == 0:
                    print("Operation cancelled.")
                    return
                
                if 1 <= choice <= len(seasons):
                    selected_season = seasons[choice - 1]
                    Season.delete_by_id(session, selected_season.id)
                    print(f"Deleted '{selected_season.name}' ({selected_season.year})")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

@cli.command('view_season')
def view_season():
    """View details of a season"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            print("No seasons found.")
            return
        
        print("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            print(f"{i}. {season.name} ({season.year})")
        
        while True:
            try:
                choice = int(input("\nEnter the number of the season to view, or 0 to cancel: "))
                if choice == 0:
                    print("Operation cancelled.")
                    return
                
                if 1 <= choice <= len(seasons):
                    selected_season = seasons[choice - 1]
                    
                    print(f"\nSeason: {selected_season.name} ({selected_season.year})\n")
                    
                    anime_series = AnimeSeries.get_all_by_season(session, selected_season.id)
                    
                    if anime_series:
                        print("Anime Series:")
                        for i, series in enumerate(anime_series, start=1):
                            print(f"{i}. {series.title}")
                        
                        while True:
                            action = input("\nEnter 'v' to view details, 'a' to add, 'd' to delete, or 'q' to quit: ").lower()
                            if action == 'q':
                                break
                            
                            elif action == 'v':
                                series_choice = int(input("Enter the number of the anime series to view: "))
                                if 1 <= series_choice <= len(anime_series):
                                    selected_series = anime_series[series_choice - 1]
                                    print(f"\nTitle: {selected_series.title}")
                                    print(f"Genre: {selected_series.genre}")
                                    print(f"Episodes: {selected_series.episodes}")
                                    print(f"Rating: {selected_series.rating:.2f}/10\n")
                                else:
                                    print("Invalid choice.")
                            
                            elif action == 'a':
                                title = input("Enter new title: ")
                                genre = input("Enter genre: ")
                                episodes = int(input("Enter number of episodes: "))
                                rating = float(input("Enter rating (out of 10): "))
                                
                                # Check if the anime series already exists
                                existing_series = session.query(AnimeSeries).filter(
                                    AnimeSeries.title == title,
                                    AnimeSeries.season_id == selected_season.id
                                ).first()
                                
                                if existing_series:
                                    print(f"'{title}' already exists in this season.")
                                else:
                                    new_series = AnimeSeries.create(session, title, genre, episodes, rating, selected_season.id)
                                    print(f"Added '{title}'")
                                
                            elif action == 'd':
                                series_choice = int(input("Enter the number of the anime series to delete: "))
                                if 1 <= series_choice <= len(anime_series):
                                    selected_series = anime_series[series_choice - 1]
                                    AnimeSeries.delete_by_id(session, selected_series.id)
                                    print(f"Deleted '{selected_series.title}'")
                                else:
                                    print("Invalid choice.")
                            
                            else:
                                print("Invalid action. Please try again.")
                    else:
                        print("No anime series found for this season.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

@cli.command('add_anime_to_season')
def add_anime_to_season():
    """Add an anime series to a season"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            print("No seasons found.")
            return
        
        print("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            print(f"{i}. {season.name} ({season.year})")
        
        while True:
            try:
                season_choice = int(input("\nEnter the number of the season to add anime to, or 0 to cancel: "))
                if season_choice == 0:
                    print("Operation cancelled.")
                    return
                
                if 1 <= season_choice <= len(seasons):
                    selected_season = seasons[season_choice - 1]
                    
                    title = input("Enter new title: ")
                    genre = input("Enter genre: ")
                    episodes = int(input("Enter number of episodes: "))
                    rating = float(input("Enter rating (out of 10): "))
                    
                    # Check if the anime series already exists
                    existing_series = session.query(AnimeSeries).filter(
                        AnimeSeries.title == title,
                        AnimeSeries.season_id == selected_season.id
                    ).first()
                    
                    if existing_series:
                        print(f"'{title}' already exists in this season.")
                    else:
                        new_series = AnimeSeries.create(session, title, genre, episodes, rating, selected_season.id)
                        print(f"Added '{title}' to season '{selected_season.name}' ({selected_season.year})")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    cli()

