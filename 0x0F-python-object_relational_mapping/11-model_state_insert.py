#!/usr/bin/python3
""" Returns  state specified bybuser in states table"""
from sqlalchemy import create_engine
from sys import argv
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
    nu_state = State(name="Louisiana")
    session.add(nu_state)
    session.commit()
    state = session.query(State).filter(State.name == "Louisiana").first()
    if state:
        print(state.id)
    else:
        print("Not found")
