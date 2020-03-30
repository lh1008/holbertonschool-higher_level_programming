#!/usr/bin/python3
""" Module that lists all states objects from a database """

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """ Main method that catches the arguments """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    sess = Session()

    make = sess.query(State).order_by(State.id).first()
    if make is None:
        print('Nothing')
    else:
        print('{}: {}'.format(make.id, make.name))

if __name__ == '__main__':
    main()
