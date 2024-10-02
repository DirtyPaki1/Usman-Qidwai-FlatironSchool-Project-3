# anime_tracker_cli.py

import click
from anime_tracker_db import Season, AnimeSeries, get_session

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
            click.echo("No seasons found.")
            return
        
        click.echo("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            click.echo(f"{i}. {season.name} ({season.year})")

@cli.command('add_season')
def add_season():
    """Add a new season"""
    name = input("Enter season name: ")
    year = int(input("Enter year: "))
    
    with get_session() as session:
        existing_season = session.query(Season).filter_by(name=name, year=year).first()
        if existing_season:
            click.echo("Season already exists.")
            return
        
        season = Season.create(session, name, year)
        click.echo(f"Added '{name}' ({year})")

@cli.command('delete_season')
def delete_season():
    """Delete a season"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            click.echo("No seasons found.")
            return
        
        click.echo("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            click.echo(f"{i}. {season.name} ({season.year})")
        
        while True:
            try:
                choice = int(input("\nEnter the number of the season to delete, or 0 to cancel: "))
                if choice == 0:
                    click.echo("Operation cancelled.")
                    return
                
                if 1 <= choice <= len(seasons):
                    selected_season = seasons[choice - 1]
                    Season.delete_by_id(session, selected_season.id)
                    click.echo(f"Deleted '{selected_season.name}' ({selected_season.year})")
                    break
                else:
                    click.echo("Invalid choice. Please try again.")
            except ValueError:
                click.echo("Invalid input. Please enter a number.")

@cli.command('view_season')
def view_season():
    """View details of a season"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            click.echo("No seasons found.")
            return
        
        click.echo("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            click.echo(f"{i}. {season.name} ({season.year})")
        
        while True:
            try:
                choice = int(input("\nEnter the number of the season to view, or 0 to cancel: "))
                if choice == 0:
                    click.echo("Operation cancelled.")
                    return
                
                if 1 <= choice <= len(seasons):
                    selected_season = seasons[choice - 1]
                    
                    click.echo(f"\nSeason: {selected_season.name} ({selected_season.year})\n")
                    
                    anime_series = AnimeSeries.get_all_by_season(session, selected_season.id)
                    
                    if anime_series:
                        click.echo("Anime Series:")
                        for i, series in enumerate(anime_series, start=1):
                            click.echo(f"{i}. {series.title}")
                        
                        while True:
                            action = input("\nEnter 'v' to view details, 'a' to add, 'd' to delete, or 'q' to quit: ").lower()
                            if action == 'q':
                                break
                            
                            elif action == 'v':
                                series_choice = int(input("Enter the number of the anime series to view: "))
                                if 1 <= series_choice <= len(anime_series):
                                    selected_series = anime_series[series_choice - 1]
                                    click.echo(f"\nTitle: {selected_series.title}")
                                    click.echo(f"Genre: {selected_series.genre}")
                                    click.echo(f"Episodes: {selected_series.episodes}")
                                    click.echo(f"Rating: {selected_series.rating:.2f}/10\n")
                                else:
                                    click.echo("Invalid choice.")
                            
                            elif action == 'a':
                                title = input("Enter new title: ")
                                genre = input("Enter genre: ")
                                episodes = int(input("Enter number of episodes: "))
                                rating = float(input("Enter rating (out of 10): "))
                                new_series = AnimeSeries.create(session, title, genre, episodes, rating, selected_season.id)
                                click.echo(f"Added '{title}'")
                            
                            elif action == 'd':
                                series_choice = int(input("Enter the number of the anime series to delete: "))
                                if 1 <= series_choice <= len(anime_series):
                                    selected_series = anime_series[series_choice - 1]
                                    AnimeSeries.delete_by_id(session, selected_series.id)
                                    click.echo(f"Deleted '{selected_series.title}'")
                                else:
                                    click.echo("Invalid choice.")
                            
                            else:
                                click.echo("Invalid action. Please try again.")
                    else:
                        click.echo("No anime series found for this season.")
                else:
                    click.echo("Invalid choice. Please try again.")
            except ValueError:
                click.echo("Invalid input. Please enter a number.")

if __name__ == '__main__':
    cli()
