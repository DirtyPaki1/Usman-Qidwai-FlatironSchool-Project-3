# anime_tracker_db.py

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declared_attr

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

engine = create_engine('sqlite:///anime_tracker.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

# Create some sample data
if __name__ == '__main__':
    session = get_session()
    
    # Ensure we're working with a fresh database
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    # Create sample seasons
    winter_2023 = Season.create(session, "Winter", 2023)
    spring_2023 = Season.create(session, "Spring", 2023)
    
    # Create sample anime series
    AnimeSeries.create(session, "Attack on Titan", "Action", 25, 9.5, winter_2023.id)
    AnimeSeries.create(session, "Demon Slayer", "Fantasy", 26, 9.0, spring_2023.id)
    
    session.close()
