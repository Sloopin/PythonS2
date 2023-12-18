import os
import sqlite3
from sqlite3 import Error
from DatabaseHelper import create
# import DatabaseHelper as mx
# mx.DatabaseHelper_function()
# from DatabaseHelper import create_connection,create,delete_raw,getalluser
# from DatabaseHelper import create
# from DatabaseHelper import delete_raw
# DatabaseHelper.DatabaseHelper_function()
os.chdir("C:\\Users\\vasil")
database_1 = "C:\\Users\\vasil\\appDB.db"
cc =create_connection(database_1)

createpersontable(cc, 'Teachers')
#om = ('MMM', 'Vaasile', 25)
#create(cc, om)
# delete_raw(cc)
# print('Tot fisierul')
# getalluser(cc)
