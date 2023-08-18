#!/usr/bin/python3
"""Print each city with each State
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    results = session.query(City, State).join(State).order_by(City.id)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
