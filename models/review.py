#!/usr/bin/python3
""" Review class for the HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ This represents a Review class.

    Attributes:
    __tablename__ (str): The name of the MySQL table to store Reviews.
    text (sqlalchemy String): The review description.
    place_id (sqlalchemy String): The review's place id.
    user_id (sqlalchemy String): The review's user id.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    text = Column(String(1024), nullable=False)
