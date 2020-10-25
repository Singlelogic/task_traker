"""This module consists of a Task class for working with events."""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Task(Base):
    """This class is used for adding tasks, changing their state,
    and searching for.
    """
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    event = Column(String(250), nullable=False)
    done = Column(String(3), nullable=False)


engine = create_engine('sqlite:///db.sqlite3', echo=False)
Base.metadata.create_all(engine)
