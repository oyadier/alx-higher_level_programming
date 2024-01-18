#!/usr/bin/python3
"""Load first rows from the db"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    usr = sys.argv[1]
    password = args[2]
    db_name = args[3]
    chemy_connect = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(chemy_connect.format(
             usr, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).first()

    if query is not None:
        print(f"{query.id}: {query.name}")
    else:
        print('Nothing')
