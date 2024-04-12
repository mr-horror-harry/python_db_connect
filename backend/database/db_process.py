from driver.db_driver import connect_db
from queries.sql_query import *
import sys

#connect to db
connection = connect_db()
cursor = connection.cursor()

if cursor:
    print("Connection successful!")
else:
    print("Connection failed!")
    exit
 
cursor.execute(CREATE_TABLE)
connection.commit()

name = sys.argv[1]
dept = sys.argv[2]
gender = sys.argv[3]
mobile = sys.argv[4]

cursor.execute(INSERT_DATA, (name, dept, gender, mobile,))
print("Data inserted successfully!")
connection.commit()