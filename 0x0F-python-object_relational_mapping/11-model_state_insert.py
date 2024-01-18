#!/usr/bin/python3
"""Add new state object"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    db_name = args[3]
    mysql_connect = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(mysql_connect.format(
             user, password, db_name, port=3360))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
