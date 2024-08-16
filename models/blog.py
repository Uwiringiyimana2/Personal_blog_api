#!/usr/bin/env python3
"""User Model"""
from models.base_model import Base, BaseModel
from datetime import datetime
from sqlalchemy import String, Integer, Column, Text, DateTime, ForeignKey


class Blog(BaseModel, Base):
    """ Blog class
    """
    __tablename__ = "blogs"
    title = Column(String(250), unique=True, nullable=False)
    content = Column(Text, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Blog({self.id} - {self.title})"
