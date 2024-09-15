from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from models import Dog, Base  # Import the Dog class and Base

def create_table(base, engine):
    """Creates the table in the database."""
    base.metadata.create_all(engine)

def save(session, dog):
    """Saves a Dog instance to the database."""
    try:
        session.add(dog)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

def get_all(session):
    """Returns a list of all Dog instances from the database."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Finds a Dog instance by its name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Finds a Dog instance by its ID."""
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    """Finds a Dog instance by its name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Updates the breed of a Dog instance."""
    try:
        dog.breed = breed
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
