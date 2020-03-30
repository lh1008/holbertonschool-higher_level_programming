#!/usr/bin/python3
""" Module that lists all states starting with N from database """
import MySQLdb
import sys


def main():
    """ Main method that catches the arguments """
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(name)s
    ORDER BY cities.id ASC""", {'name': name})
    grab = cur.fetchall()
    print(", ".join(row[0] for row in grab))

if __name__ == '__main__':
    main()
