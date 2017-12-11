# config/database.py
import pymongo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

Base = declarative_base()

engine_accesos = create_engine('sqlite:///db/db_accesos.db')
session_accesos = sessionmaker()
session_accesos.configure(bind=engine_accesos)

db_peru_gis = MongoClient('mongodb://localhost:27017/')['peru-gis']