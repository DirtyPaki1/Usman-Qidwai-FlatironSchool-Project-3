from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Season(Base):
    __tablename__ = 'seasons'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    anime_series = relationship("AnimeSeries", back_populates="season")

    def __repr__(self):
        return f"<Season(id={self.id}, name='{self.name}', year={self.year})>"

class AnimeSeries(Base):
    __tablename__ = 'anime_series'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    episodes = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    season_id = Column(Integer, ForeignKey('seasons.id'), nullable=False)
    season = relationship("Season", back_populates="anime_series")

    def __repr__(self):
        return f"<AnimeSeries(id={self.id}, title='{self.title}', genre='{self.genre}', episodes={self.episodes}, rating={self.rating}, season_id={self.season_id})>"

def get_session():
    engine = create_engine('sqlite:///anime_tracker.db')
    Session = sessionmaker(bind=engine)
    return Session()

def close_connection(session):
    session.close()

def initialize_database():
    engine = create_engine('sqlite:///anime_tracker.db')
    Base.metadata.create_all(engine)
