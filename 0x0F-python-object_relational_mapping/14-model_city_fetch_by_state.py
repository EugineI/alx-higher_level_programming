#!/usr/bin/python3
"""
cities
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import State, Base

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2].replace('@', '%40')
    database = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, database),
            pool_pre_ping=True
            )
    Base.metadata.bind = engine
    NewSession = sessionmaker(bind=engine)
    session = NewSession()

    cities = (
            session.query(City, State)
            .join(State, City.state_id == State.id)
            .order_by(City.id.asc())
            .all()
            )
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
