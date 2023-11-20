#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    NewState = State(name='California')
    NewCity = City(name='San Francisco')
    NewState.cities.append(NewCity)

    session.add(NewState)
    session.add(NewCity)
    session.commit()
    session.close()
