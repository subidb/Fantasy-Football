import prem_fantasy
import time
from game_class import AppUser, Player, UserPoints
from game_sql import appuser_add_entry
import getpass


def login_screen(): # takes in the login info and passes it for validation from gmail and a possible email send
    em1 = input("\nEnter your email: ")
    passw = getpass.getpass('Enter your password: ')
    prem_fantasy.check_and_send(em1, em1, passw)


def sign_up():
    # taking in valid user signup details with rules for password and username,
    # if valid, passing it to the functions that send the details to mysql database
    # and send a confirmation email to the user using http requests
    while True: 
        email = input("\nEmail: ")
        passwd = getpass.getpass("Password: ")
        username = input("Create Username: ")
        if email.find("@") > 0 and email.find(".com") > 3 and len(passwd) > 5 and len(username) > 5:
            break
        else:
            print("Invalid Registration details!. Enter a valid email, password and username must be atleast 6 digits")

    create_user(email, username, passwd)
    content = ["Welcome to Fantasy Football 2.0!", "Hi {}, \n\n Your signup is successful!, \n".format(username)
               + "You can now login to continue: https://fantasy.premierleague.com/"]

    prem_fantasy.send_email(email, email, passwd, content) 
    print("Registration Succesful, you can now play the game!")


# creating a user object through the sign up details,
# passing the object to a function which will parse and add it to the database
def create_user(email, username, pw):  
    user = AppUser(1, username, email, pw, 0)
    appuser_add_entry(user)


logsign = input("Press L to Login, S to Sign up: ")

while True:
    if logsign in "Ll":
        login_screen()
        break
    if logsign in "Ss":
        sign_up()
        break
    logsign = input("Press L to Login, S to Sign up: ")


    

