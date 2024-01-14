#!/usr/bin/python3
'''Filter states by user input'''
import MySQLdb
import sys


def search_by_input(username, password, name, searched):
    '''Take argument and display state
        Arg:
            username (string): db user name
            password (int): password of the db
            name (string): db name
            searched (string): keyword to search for
    '''
    con = MySQLdb.connect(host="localhost",
                          port=3360,
                          user=username,
                          db=name)
    cur = con.cursor()
    query = "SELECT * FROM states WHERE name=('{}')".format(searched)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        if (rows[1] == searched):
            print(row)
    cur.close()
    con.close()

if __name__ == "__main__":
    arg = sys.argv
    user = arg[1]
    usr_passwd = arg[2]
    db_name = arg[3]
    search_ky = arg[4]
    search_by_input(user, usr_passwd, db_name, search_ky)
