#!/usr/bin/python3
"""Import declarativ clase and class state"""


from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
import urllib.parse

if __name__ == '__main__':
    user = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = (update(State).where(
        State.id == 2).values(name='New Mexico'))
    session.execute(update_state)
    session.commit()
