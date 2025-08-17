from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class Animals(Base):
    __tablename__ = 'animals'

id = Column(Integer, primary_key=True, index=True)
name = Column(String, nullable=False)
age = Column(Integer, nullable=False)
adopted = Column(Boolean, nullable=False)