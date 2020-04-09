import requests
from bs4 import BeautifulSoup
import inspect
import smtplib
import time
import getpass
import re

# URL = 'https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/
# ref=sr_1_4?dchild=1&keywords=airpods+pro&qid=1585944327&sr=8-4 '
# URL = 'https://www.premierleague.com/stats/top/players/'
URL = 'https://www.bbc.com/sport/football/premier-league/top-scorers'

headers1 = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.149 Safari/537.36'
}


def check_and_send(e1, e2, pw):  # function to add a body and subject to the email and pass the login deails to the user 
    while True:
        getans = input("Activate Player Updates? (Y/N): ")
        if getans in "Yy":
            text1 = "Futwiz Fantasy updates turned on!\n\n You will now receive updates on player prices, player statistics on"\
                    " your email. Keep the notifications on!"
            send_email(e1, e2, pw, ["Fantasy football 2.0", text1])
            return
        elif getans in "Nn":
            return
        else:
            pass



def check_ratings():  # scrapes and extracts data from the premier league wesbite

    page = requests.get(URL, headers=headers1)  # storing the data in variable

    soup = BeautifulSoup(page.content, 'html.parser')  # storing the parsed data in variable
    # soup = BeautifulSoup(page.content, "lxml")

    # finding, extracting data attributes through the respective html classes and ids
    namerow = soup.find_all(class_="top-player-stats__name gel-double-pica")
    goalsrow = soup.find_all(class_="top-player-stats__goals-scored-number")
    assistsrow = soup.find_all(class_="top-player-stats__assists-number gel-double-pica")


# check_ratings()


def send_email(email1, email2, passwd, content):  # content = List[(Email subject), (body)]

    server = smtplib.SMTP('smtp.gmail.com', 587)  # gmail protocal
    server.ehlo()  # command sent by an email server to identify itself connecting to another email
    server.starttls()  # encrypts connection
    server.ehlo()

    # server.login('subid.basaula@gmail.com', 'vmtc urju mcoz omyf')

    try:
        server.login(email1, passwd)
    except:
        print("\nInvalid Email/Password!\n")
        raise SystemExit

    # parsing the data and sending the mail
    subject = content[0]
    body = '\n {}'.format(content[1]) 
    message = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        email1,
        email2,
        message
    )

    print("\nEmail has been sent!")

    server.quit()

