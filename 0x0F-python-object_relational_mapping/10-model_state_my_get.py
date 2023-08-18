#!/usr/bin/python3
"""List all States that have letter 'a' in their name from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    try:
        state = session.query(State).filter(
            State.name.regexp_match(sys.argv[4])).order_by(
            State.id).limit(1).one()
        print("{}: {}".format(state.id, state.name))
    except NoResultFound:
        print("Not found")

    session.close()
