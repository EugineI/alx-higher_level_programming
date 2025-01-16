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
    state_name = sys.argv[4]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(username, password, database),
            pool_pre_ping=True
        )
    Base.metadata.bind = engine
    NewSession = sessionmaker(bind=engine)
    session = NewSession()
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()