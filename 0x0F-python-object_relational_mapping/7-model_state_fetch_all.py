#!/usr/bin/python3
"""
list states
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username,
                password,
                database
                ),
            pool_pre_ping=True
            )
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}:{}".format(state.id, state.name))
    session.close()
