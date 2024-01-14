#!/usr/bin/python3
'''A function to search for state by initials'''
import MySQLdb
import sys


def search_filter(username, password, name):
    '''script that lists all states with a name
        starting with N (upper N) from the database hbtn_0e_0_usa:
        Arg:
            username (string): db user
            password (int): password of the db
            name (string): name of the db
    '''
    con = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=username,
                          passwd=password,
                          db=name,
                          charset='utf8')
    curs = con.cursor()
    curs.execute(f"SELECT * FROM `states` WHERE `name`\
                LIKE 'N%' ORDER BY `id` ASC")
    rows = curs.fetchall()

    for row in rows:
        if ("N" in row[1]):
            print(row)

    curs.close()
    con.close()


if __name__ == "__main__":
    arg_list = sys.argv
    user_name = arg_list[1]
    pass_code = arg_list[2]
    db_name = arg_list[3]
    search_filter(user_name, pass_code, db_name)
