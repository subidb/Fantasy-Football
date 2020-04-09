import mysql.connector
import getpass
from game_class import AppUser, Player
from z_extra_codesnippets import tuples_list
pw = getpass.getpass('Enter your server password: ')

#validating password and connecting to the local mysql database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pw,
    database="AppDB"
)

print("Connection successful. \n")

cursor = db.cursor() # a cursor to for database manipulation and queries

#Functions for database manipulation and queries 

def appuser_add_entry(obj):
    q1 = " INSERT INTO appusers (username, email, passwd) VALUES (%s, %s, %s)"
    cursor.execute(q1, (obj.username, obj.email, obj.passwd))
    db.commit()


