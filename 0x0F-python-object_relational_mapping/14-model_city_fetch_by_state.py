#!/usr/bin/python3
""" Returns cities in vities table"""
from sqlalchemy import create_engine
from sys import argv
from model_city import Base, City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    user, pw, name = argv[1], argv[2], argv[3]
    db = 'mysql+mysqldb'
    host = 'localhost'
    port = '3306'
    const = "{}://{}:{}@{}:{}/{}".format(db, user, pw, host, port, name)
    engine = create_engine(const, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    locatn = session.query(City, State).join(State).all()
    for city, state in locatn:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
