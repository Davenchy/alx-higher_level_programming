#!/usr/bin/python3
"""Print each state with cities belong to it"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    states = session.query(City.id, City.name, State.name).join(
        State).order_by(City.id).all()

    for id, city, state in states:
        print("{}: {} -> {}".format(id, city, state))

    session.close()
