# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine_accesos = create_engine('sqlite:///db/db_accesos.db')
session_accesos = sessionmaker()
session_accesos.configure(bind=engine_accesos)
