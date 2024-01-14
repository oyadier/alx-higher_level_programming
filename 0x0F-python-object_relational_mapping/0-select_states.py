#!/usr/bin/python3
import sys
import MySQLdb

'''Using MySQLdb module to access and print rows in db'''
arg = sys.argv
usr = arg[1]
password = arg[2]
db_name = arg[3]

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
