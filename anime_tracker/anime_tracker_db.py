import click
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declared_attr

# Database Setup
Base = declarative_base()

class Season(Base):
    __tablename__ = 'seasons'
    
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True)
    
    name = Column(String(50), unique=True)
    year = Column(Integer)
    
    @property
    def full_name(self):
        return f"{self.name} ({self.year})"
    
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def create(cls, session, name, year):
        season = cls(name=name, year=year)
        session.add(season)
        session.commit()
        return season
    
    @classmethod
    def delete_by_id(cls, session, id):
        season = session.query(cls).get(id)
        if season:
            session.delete(season)
            session.commit()
            return True
        return False

class AnimeSeries(Base):
    __tablename__ = 'anime_series'
    
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True)
    
    title = Column(String(100))
    genre = Column(String(50))
    episodes = Column(Integer)
    rating = Column(Float)
    season_id = Column(Integer, ForeignKey('seasons.id'))
    
    @property
    def season(self):
        return Season.query.get(self.season_id)
    
    @classmethod
    def get_all_by_season(cls, session, season_id):
        return session.query(cls).filter_by(season_id=season_id).all()
    
    @classmethod
    def create(cls, session, title, genre, episodes, rating, season_id):
        series = cls(title=title, genre=genre, episodes=episodes, rating=rating, season_id=season_id)
        session.add(series)
        session.commit()
        return series
    
    @classmethod
    def delete_by_id(cls, session, id):
        series = session.query(cls).get(id)
        if series:
            session.delete(series)
            session.commit()
            return True
        return False

# CLI Setup
engine = create_engine('sqlite:///anime_tracker.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

@click.group()
def cli():
    """Anime Tracker CLI"""
    pass

@cli.command('list_seasons')
def list_seasons():
    """List all seasons"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            click.echo("No seasons found.")
            return
        
        click.echo("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            click.echo(f"{i}. {season.full_name}")

@cli.command('add_season')
def add_season():
    """Add a new season"""
    name = click.prompt("Enter season name", type=str)
    year = click.prompt("Enter year", type=int)
    
    with get_session() as session:
        existing_season = session.query(Season).filter_by(name=name, year=year).first()
        if existing_season:
            click.echo(f"Season '{name}' ({year}) already exists.")
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
            click.echo(f"{i}. {season.full_name}")
        
        while True:
            try:
                choice = click.prompt(
                    "Enter the number of the season to delete, or 0 to cancel",
                    type=int,
                    default=-1
                )
                if choice == 0:
                    click.echo("Operation cancelled.")
                    return
                
                if 1 <= choice <= len(seasons):
                    selected_season = seasons[choice - 1]
                    if Season.delete_by_id(session, selected_season.id):
                        click.echo(f"Deleted '{selected_season.name}' ({selected_season.year})")
                    else:
                        click.echo("Failed to delete the season.")
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
            click.echo(f"{i}. {season.full_name}")
        
        while True:
            try:
                choice = click.prompt(
                    "Enter the number of the season to view, or 0 to cancel",
                    type=int,
                    default=-1
                )
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
                            action = click.prompt(
                                "Enter 'v' to view details, 'a' to add, 'd' to delete, or 'q' to quit",
                                type=str.lower,
                                default=""
                            ).strip()
                            if action == 'q':
                                break
                            
                            elif action == 'v':
                                series_choice = click.prompt(
                                    "Enter the number of the anime series to view",
                                    type=int,
                                    default=-1
                                )
                                if 1 <= series_choice <= len(anime_series):
                                    selected_series = anime_series[series_choice - 1]
                                    click.echo(f"\nTitle: {selected_series.title}")
                                    click.echo(f"Genre: {selected_series.genre}")
                                    click.echo(f"Episodes: {selected_series.episodes}")
                                    click.echo(f"Rating: {selected_series.rating:.2f}/10\n")
                                else:
                                    click.echo("Invalid choice.")
                            
                            elif action == 'a':
                                title = click.prompt("Enter new title", type=str)
                                genre = click.prompt("Enter genre", type=str)
                                episodes = click.prompt("Enter number of episodes", type=int)
                                rating = click.prompt("Enter rating (out of 10)", type=float)
                                new_series = AnimeSeries.create(session, title, genre, episodes, rating, selected_season.id)
                                click.echo(f"Added '{title}'")
                            
                            elif action == 'd':
                                series_choice = click.prompt(
                                    "Enter the number of the anime series to delete",
                                    type=int,
                                    default=-1
                                )
                                if 1 <= series_choice <= len(anime_series):
                                    selected_series = anime_series[series_choice - 1]
                                    if AnimeSeries.delete_by_id(session, selected_series.id):
                                        click.echo(f"Deleted '{selected_series.title}'")
                                    else:
                                        click.echo("Failed to delete the anime series.")
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

@cli.command('add_anime_to_season')
def add_anime_to_season():
    """Add an anime series to a season"""
    with get_session() as session:
        seasons = Season.get_all(session)
        if not seasons:
            click.echo("No seasons found.")
            return
        
        click.echo("\nAvailable Seasons:")
        for i, season in enumerate(seasons, start=1):
            click.echo(f"{i}. {season.full_name}")
        
        while True:
            try:
                choice = click.prompt(
                    "Enter the number of the season to add anime to, or 0 to cancel",
                    type=int,
                    default=-1
                )
                if choice == 0:
                    click.echo("Operation cancelled.")
                    return
                
                if 1 <= choice <= len(seasons):
                    selected_season = seasons[choice - 1]
                    
                    title = click.prompt("Enter anime series title", type=str)
                    genre = click.prompt("Enter genre", type=str)
                    episodes = click.prompt("Enter number of episodes", type=int)
                    rating = click.prompt("Enter rating (out of 10)", type=float)
                    
                    new_series = AnimeSeries.create(session, title, genre, episodes, rating, selected_season.id)
                    click.echo(f"Added '{title}' to season '{selected_season.name}' ({selected_season.year})")
                    break
                else:
                    click.echo("Invalid choice. Please try again.")
            except ValueError:
                click.echo("Invalid input. Please enter a number.")

if __name__ == '__main__':
    cli()

