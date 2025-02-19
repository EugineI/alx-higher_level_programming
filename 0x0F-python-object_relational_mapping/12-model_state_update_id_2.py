#!/usr/bin/python3
"""
change name of a state
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

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
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()
