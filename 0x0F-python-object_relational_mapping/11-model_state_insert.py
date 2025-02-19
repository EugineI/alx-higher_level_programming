#!/usr/bin/python3
"""
inser a new state
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2].replace('@', '%40')
    database = sys.argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database),
            pool_pre_ping=True
        )
    Base.metadata.bind = engine
    NewSession = sessionmaker(bind=engine)
    session = NewSession()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
