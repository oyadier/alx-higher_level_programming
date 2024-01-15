#!/usr/bin/python3
'''Load rows from two table using JOIN'''
import sys
import MySQLdb


def list_cities(username, password, db, state_name):
    '''Using MySQLdb module to access and print rows in db
        Args:
            username (string): the name of the db user
            passward (int): the dscode
            db (string): the name of the database
    '''
    con = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=usr,
                          passwd=password,
                          db=db_name,
                          charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT cities.name FROM\
            `cities` JOIN `states` ON state_id=states.id\
            WHERE states.name=(%s)\
            ORDER BY cities.id", [state_name])
    all_row = cur.fetchall()

    city = ""
    for row in all_row:
        for cm in row:
            city += (cm) + ", "
    print(city[:-2])

    cur.close()
    con.close()


if __name__ == "__main__":
    arg = sys.argv
    usr = arg[1]
    password = arg[2]
    db_name = arg[3]
    state = arg[4]
    list_cities(usr, password, db_name, state)
