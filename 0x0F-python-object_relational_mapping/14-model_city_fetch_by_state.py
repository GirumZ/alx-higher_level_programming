#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    s_c = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in s_c:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
