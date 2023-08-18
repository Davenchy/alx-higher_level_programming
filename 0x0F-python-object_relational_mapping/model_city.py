#!/usr/bin/python3
"""The City class definition for the ORM"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """The City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return "City(id: {}, name: {}, state_id: {})".format(self.id,
                                                             self.name,
                                                             self.state_id)
