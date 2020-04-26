from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core import config

engine = create_engine(config.SQLALCHEMY_URI)
Session = sessionmaker(bind=engine)
