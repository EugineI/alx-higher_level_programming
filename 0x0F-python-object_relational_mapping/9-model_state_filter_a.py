#!/usr/bin/python3
"""
first state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2].replace('@', '%40')
    database = sys.argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(username, password, database),
            pool_pre_ping=True
        )
    Base.metadata.bind = engine
    NewSession = sessionmaker(bind=engine)
    session = NewSession()
    states = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id.asc())
            .all()
            )
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
