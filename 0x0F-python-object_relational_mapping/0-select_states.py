#!/usr/bin/python3
'''Using MySQLdb module to access and print rows in db'''
import sys
import MySQLdb


def select_rows(username, password, db):
    '''Using MySQLdb module to access and print rows in db
        Args:
            username (string): the name of the db user
            passward (int): the db passcode
            db (string): the name of the database
    '''
    con = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=usr,
                          passwd=password,
                          db=db_name,
                          charset="utf8")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM `states` ORDER BY id ASC")
    all_row = cur.fetchall()

    for row in all_row:
        print(row)

    cur.close()
    con.close()


if __name__ == "__main__":
    arg = sys.argv
    usr = arg[1]
    password = arg[2]
    db_name = arg[3]
    select_rows(usr, password, db_name)
