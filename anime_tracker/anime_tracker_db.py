import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

# Database setup
engine = create_engine('sqlite:///anime_tracker.db')
Base = declarative_base()

# Define database models
class AnimeShow(Base):
    __tablename__ = 'anime_shows'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    total_episodes = Column(Integer, nullable=False)
    current_episode = Column(Integer, nullable=False)
    episodes = relationship("Episode", backref="anime_show")
    characters = relationship("Character", backref="anime_show")

    def __repr__(self):
        return f"<AnimeShow(id={self.id}, title='{self.title}', genre='{self.genre}', total_episodes={self.total_episodes}, current_episode={self.current_episode})>"

class Episode(Base):
    __tablename__ = 'episodes'
    
    id = Column(Integer, primary_key=True)
    episode_number = Column(Integer, nullable=False)
    air_date = Column(Date, nullable=False)
    watched = Column(Boolean, default=False)
    rating = Column(Float, nullable=True)
    review = Column(String, nullable=True)
    anime_show_id = Column(Integer, ForeignKey('anime_shows.id'), nullable=False)

    def __repr__(self):
        return f"<Episode(id={self.id}, episode_number={self.episode_number}, air_date={self.air_date}, watched={self.watched})>"

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    anime_show_id = Column(Integer, ForeignKey('anime_shows.id'), nullable=False)

    def __repr__(self):
        return f"<Character(id={self.id}, name='{self.name}', description='{self.description}')>"

# ORM methods
def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

def initialize_database():
    Base.metadata.create_all(engine)

def add_anime_show(session, title, genre, total_episodes):
    show = AnimeShow(title=title, genre=genre, total_episodes=total_episodes, current_episode=0)
    session.add(show)
    session.commit()
    print(f"Added anime show: {show.title}")

def get_all_anime_shows(session):
    return session.query(AnimeShow).all()

def delete_anime_show(session, show_id):
    show = session.query(AnimeShow).filter_by(id=show_id).first()
    if show:
        session.delete(show)
        session.commit()
        print(f"Deleted anime show: {show.title}")
    else:
        print("Anime show not found.")

def add_episode(session, show_id, episode_number, air_date):
    show = session.query(AnimeShow).filter_by(id=show_id).first()
    if show:
        episode = Episode(episode_number=episode_number, air_date=air_date, anime_show_id=show_id)
        session.add(episode)
        session.commit()
        print(f"Added episode {episode_number} for {show.title}")
    else:
        print("Anime show not found.")

def mark_episode_watched(session, episode_id):
    episode = session.query(Episode).filter_by(id=episode_id).first()
    if episode:
        episode.watched = True
        session.commit()
        print(f"Marked episode {episode.episode_number} of {episode.anime_show.title} as watched.")
    else:
        print("Episode not found.")

def add_character(session, show_id, name, description):
    show = session.query(AnimeShow).filter_by(id=show_id).first()
    if show:
        character = Character(name=name, description=description, anime_show_id=show_id)
        session.add(character)
        session.commit()
        print(f"Added character {character.name} to {show.title}")
    else:
        print("Anime show not found.")

def rate_episode(session, episode_id, rating):
    episode = session.query(Episode).filter_by(id=episode_id).first()
    if episode:
        episode.rating = rating
        session.commit()
        print(f"Rated episode {episode.episode_number} of {episode.anime_show.title} with {rating}/10")
    else:
        print("Episode not found.")

def review_episode(session, episode_id, review):
    episode = session.query(Episode).filter_by(id=episode_id).first()
    if episode:
        episode.review = review
        session.commit()
        print(f"Added review for episode {episode.episode_number} of {episode.anime_show.title}")
    else:
        print("Episode not found.")
