#!/usr/bin/python3
""" Module that lists all states objects from a database """

from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """ Main method that catches the arguments """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2],
                                                    argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    sess = Session()

    for s, c in sess.query(State, City).\
            filter(State.id == City.state_id).all():
        print('{}: ({}) {}'.format(s.name, c.id, c.name))

if __name__ == '__main__':
    main()
