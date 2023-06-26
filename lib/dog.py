from models import Dog
from sqlalchemy import (create_engine, desc,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def create_table(base, engine):
    __tablename__ = 'dogs'

    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    grade = Column(Integer())

if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs
def find_by_name(session, name):
    doggie = session.query(Dog).filter(Dog.name.like(f'{name}')).one()
    # dog = session.query(Dog).filter(Dog.name == name).one()
    # return dog
    return doggie

def find_by_id(session, id):
    doggie = session.query(Dog).filter(Dog.id.like(f'{id}')).one()
    return doggie

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name.like(f'{name}'),
        Dog.breed == breed).one()
    return query

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()