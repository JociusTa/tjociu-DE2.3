from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, create_engine, UniqueConstraint, func, text,Table,MetaData
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declared_attr
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

Base = declarative_base()


class Cities(Base):
    """
    Table to hold data of largest cities in Europe
    """
    __tablename__= "JOBS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    link = Column(String)
    type = Column(String(20))
    region = Column(String)
    salary = Column(String)
    added_at = Column(DateTime)
    _
