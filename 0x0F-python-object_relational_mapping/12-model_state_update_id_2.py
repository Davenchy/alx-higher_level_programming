#!/usr/bin/python3
"""rename a state of id 2 to New Mexico
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    state = session.query(State).get(2)
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()
