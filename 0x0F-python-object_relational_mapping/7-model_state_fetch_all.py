#!/usr/bin/python3
"""Import declarativ clase and class state"""


from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
import urllib.parse

user = sys.argv[1]
password = urllib.parse.quote_plus(sys.argv[2])
database = sys.argv[3]

engine = create_engine(
    f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}")
Session = sessionmaker(bind=engine)
session = Session()
our_states = session.query(State).order_by(State.id)
for state in our_states:
    print(f"{state.id}: {state.name}")
