#!/usr/bin/python3
"""Import declarativ clase and class state"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
import urllib.parse

if __name__ == '__main__':
    user = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]
    state_name = State(name='Louisiana')
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(state_name)
    session.flush()
    print(state_name.id)
