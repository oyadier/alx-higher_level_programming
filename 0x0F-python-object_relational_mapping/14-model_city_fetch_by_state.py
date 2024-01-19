#!/usr/bin/python3
"""Pirnting all City objects"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import Base, City
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
    cities = session.query(State.name, City.id, City.name)\
                    .join(City, City.state_id == State.id)\
                    .order_by(City.id).all()
    for city in cities:
        print(f"{city[0]}: ({city.id}) {city.name}")
