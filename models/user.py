#!/usr/bin/env python3
"""User Model"""
from models.base_model import Base, BaseModel
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from models.blog import Blog


class User(BaseModel, Base):
    """ User class
    """
    __tablename__ = "users"
    email = Column(String(120), unique=True, nullable=False)
    firstName = Column(String(120), nullable=False)
    lastName = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    blogs = relationship("Blog", backref="author", cascade="all, delete-orphan", lazy=True)

    def __repr__(self) -> str:
        return f"User({self.id} - {self.firstName} {self.lastName})"
