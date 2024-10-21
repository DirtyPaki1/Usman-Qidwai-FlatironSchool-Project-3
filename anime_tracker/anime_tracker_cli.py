import click
from anime_tracker_db import get_session, initialize_database, AnimeShow, Episode, Character
from datetime import date

# CLI helper functions
def display_anime_shows(shows):
    click.echo("\nAvailable Anime Shows:")
    for i, show in enumerate(shows, start=1):
        click.echo(f"{i}. {show.title}")

def display_episodes(episodes):
    click.echo("\nAvailable Episodes:")
    for i, episode in enumerate(episodes, start=1):
        watched_status = "Watched" if episode.watched else "Not Watched"
        click.echo(f"{i}. Episode {episode.episode_number} ({watched_status})")

def display_characters(characters):
    click.echo("\nCharacters:")
    for i, character in enumerate(characters, start=1):
        click.echo(f"{i}. {character.name}")

# Main CLI application
@click.group()
def cli():
    """Anime Tracker CLI"""
    pass

@cli.command()
def initialize():
    """Initialize the database"""
    initialize_database()
    click.echo("Database initialized successfully.")

@cli.command()
@click.option('--title', prompt='Enter anime show title')
@click.option('--genre', prompt='Enter genre')
@click.option('--total-episodes', prompt='Enter total episodes', type=int)
def add_show(title, genre, total_episodes):
    """Add a new anime show"""
    session = get_session()
    from anime_tracker_db import add_anime_show
    add_anime_show(session, title, genre, total_episodes)
    close_connection(session)

@cli.command()
def list_shows():
    """List all anime shows"""
    session = get_session()
    from anime_tracker_db import get_all_anime_shows
    shows = get_all_anime_shows(session)
    display_anime_shows(shows)
    close_connection(session)

@cli.command()
@click.option('--show-id', prompt='Enter ID of the anime show to delete', type=int)
def delete_show(show_id):
    """Delete an anime show"""
    session = get_session()
    from anime_tracker_db import delete_anime_show
    delete_anime_show(session, show_id)
    close_connection(session)

@cli.command()
@click.option('--show-id', prompt='Enter ID of the anime show', type=int)
@click.option('--episode-number', prompt='Enter episode number', type=int)
@click.option('--air-date', prompt='Enter air date (YYYY-MM-DD)', type=str)
def add_episode(show_id, episode_number, air_date):
    """Add a new episode to an anime show"""
    session = get_session()
    from anime_tracker_db import add_episode
    add_episode(session, show_id, int(episode_number), date.fromisoformat(air_date))
    close_connection(session)

@cli.command()
@click.option('--episode-id', prompt='Enter ID of the episode to mark as watched', type=int)
def watch_episode(episode_id):
    """Mark an episode as watched"""
    session = get_session()
    from anime_tracker_db import mark_episode_watched
    mark_episode_watched(session, episode_id)
    close_connection(session)

@cli.command()
@click.option('--show-id', prompt='Enter ID of the anime show', type=int)
@click.option('--name', prompt='Enter character name')
@click.option('--description', prompt='Enter character description')
def add_character(show_id, name, description):
    """Add a character to an anime show"""
    session = get_session()
    from anime_tracker_db import add_character
    add_character(session, show_id, name, description)
    close_connection(session)

@cli.command()
@click.option('--episode-id', prompt='Enter ID of the episode to rate', type=int)
@click.option('--rating', prompt='Enter rating (1-10)', type=float)
def rate(episode_id, rating):
    """Rate an episode"""
    session = get_session()
    from anime_tracker_db import rate_episode
    rate_episode(session, episode_id, rating)
    close_connection(session)

@cli.command()
@click.option('--episode-id', prompt='Enter ID of the episode to review', type=int)
@click.option('--review', prompt='Enter your review')
def review(episode_id, review):
    """Review an episode"""
    session = get_session()
    from anime_tracker_db import review_episode
    review_episode(session, episode_id, review)
    close_connection(session)

@cli.command()
@click.option('--show-id', prompt='Enter ID of the anime show', type=int)
def view_show(show_id):
    """View details of an anime show"""
    session = get_session()
    shows = session.query(AnimeShow).filter_by(id=show_id).all()
    if shows:
        show = shows[0]
        click.echo(f"\n{show.title} ({show.genre})")
        click.echo(f"Total Episodes: {show.total_episodes}")
        click.echo(f"Current Episode: {show.current_episode}")
        
        episodes = session.query(Episode).filter_by(anime_show_id=show.id).all()
        display_episodes(episodes)
        
        characters = session.query(Character).filter_by(anime_show_id=show.id).all()
        display_characters(characters)
    else:
        click.echo("Anime show not found.")
    close_connection(session)

def close_connection(session):
    session.close()

if __name__ == '__main__':
    cli()
