import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from .models import metadata

database_path = Path() / os.path.dirname(os.path.abspath(__file__)) / "example.db"
engin = create_engine(f"sqlite:///{database_path}")


def init_database() -> "scoped_session":
    if not os.path.isfile(database_path):
        Path(database_path).touch()
    metadata.create_all(bind=engin, checkfirst=True)
    Session = scoped_session(sessionmaker(bind=engin))
    return Session



        
