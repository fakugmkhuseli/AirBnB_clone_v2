#!/usr/bin/python3
""" State class for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ This represents an Amenity class.

    Attributes:
    __tablename__(str): The name of the MySQL table to store Amenities.
    name (sqlalchemy String):L The amenity name.
    place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
