#!/usr/bin/python3
"""Pirnting all state"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    arg = sys.argv
    usr = arg[1]
    password = arg[2]
    db_name = arg[3]
    mysql_connection = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(mysql_connection.format(
             usr, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).all()
    for s in query:
        print(f"{s.id}: {s.name}")
