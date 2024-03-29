#!/usr/bin/python3
"""
 A python file that contains the class definition of
 a State and an instance Base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class defination of state """

    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, nullable=False, autoincrement="auto"
    )
    name = Column(String(128), nullable=False)
