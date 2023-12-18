import os
import sqlite3
from sqlite3 import Error
os.chdir("C:\\Users\\vasil")


def create_connection(db_file):

    c = None
    try:
        c = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return c


def createpersontable(conn_1, table_name):

    command1 = "CREATE TABLE IF NOT EXISTS "+table_name+"(ID INT PRIMARY KEY, First_Name CHAR(25) NOT NULL, Last_Name CHAR(25), Age INT)"
    cur = conn.cursor()
    cur.execute(command1)
    conn_1.commit()


def create(conn_1, task):
   
    sql_insert = "INSERT INTO Person (First_Name,Last_Name,age) VALUES (?,?,?)"
    cur = conn.cursor()
    cur.execute(sql_insert, task)
    conn_1.commit()
    return cur.lastrowid


def read():
    sql_read = "SELECT * FROM  Person WHERE First_Name  LIKE '%Po%'"
    cur = conn.cursor()
    cur.execute(sql_read)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def update(conn_1, task):
    sql_update = "UPDATE Person SET First_Name = ?, Last_Name = ?, age = ? WHERE  First_Name  LIKE '%Po%'"
    cur = conn_1.cursor()
    cur.execute(sql_update, task)
    conn_1.commit()


def delete_row(conn_1):
    sql_delete_row = "DELETE FROM Person WHERE First_Name LIKE '%Po%' "
    cur = conn_1.cursor()
    cur.execute(sql_delete_row)
    conn_1.commit()


def delete_all_tasks(conn_1):

    sql_delete_all = "DELETE FROM Person"
    cur = conn_1.cursor()
    cur.execute(sql_delete_all)
    conn_1.commit()


def getalluser(conn_1):
    sql_getalluser = "SELECT * from Person"
    cur = conn_1.cursor()
    cur.execute(sql_getalluser)
    rows = cur.fetchall()
    for row in rows:
        print(row)


database = "C:\\Users\\vasil\\appDB.db"
conn = create_connection(database)

createpersontable(conn,'Person')
Pers1 = ('Pop', 'Vasile', 35)
create(conn, Pers1)
Pers2 = ('Ion', 'Vasile', 15)
create(conn, Pers2)
print("Insert")
read()
pers3 = ('Pop', 'Mihai', 40)
update(conn, pers3)
print("Update")
read()
delete_row(conn)
getalluser(conn)
# delete_all_tasks(conn)
