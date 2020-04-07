#!/usr/bin/python3
""" Module that lists all states objects from a database """

from model_state import Base, State
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

    sess.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    sess.commit()

if __name__ == '__main__':
    main()
