import mysql.connector
import getpass
from game_class import AppUser, Player
from z_extra_codesnippets import tuples_list
pw = getpass.getpass('Enter your server password: ')

# validating password and connecting to the local mysql database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pw,
    database="AppDB"
)

print("Connection successful. \n")

cursor = db.cursor() # a cursor to for database manipulation and queries

# Functions for database manipulation and queries 

def appuser_add_entry(obj):
    q1 = " INSERT INTO appusers (username, email, passwd) VALUES (%s, %s, %s)"
    cursor.execute(q1, (obj.username, obj.email, obj.passwd))
    db.commit()


def points_add_entry(ptuple):
    q1 = "INSERT INTO userpoints (userpoints_id, week1, week2, week3, total_points) VALUES (%s, %s, %s, %s, %s)"
    for pts_tuple in ptuple:
        cursor.execute(q1, pts_tuple)
    db.commit()
 

def appuser_selectall():
    q1 = "SELECT * FROM appusers"
    cursor.execute(q1)


def userpoints_selectall():
    q1 = "SELECT * FROM userpoints"
    cursor.execute(q1)


def usernum():
    print("Total number of users = ")
    q1 = "SELECT COUNT(user_id) FROM appusers"
    cursor.execute(q1)


# Displays the Ranking sorted by points by Joining tables appusers and userpoints, using foreign keys of userpoints table 
def showrankings():
    print("RANKING TABLE:")
    q1 = "SELECT appusers.username, userpoints.total_points \
        FROM appusers \
        JOIN userpoints ON appusers.user_id = userpoints.userpoints_id \
        ORDER BY total_points DESC"
    cursor.execute(q1)


# appuser_selectall()
# for user in cursor:
#     print(user)

showrankings()
for points in cursor:
    print(points)

