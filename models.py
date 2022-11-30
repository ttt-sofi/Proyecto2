from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True, index=True)
    nombre_region = Column(String(255), unique=True)
