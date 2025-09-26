from .database import Base, engine
from model.Enterprise import Enterprise
from model.EletronicPart import EletronicPart  # importe todos os models


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables Createad")