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


def parse_and_return(row1, row2, row3):  # row'i' = data scraped from webpage using bs4
    # extracting required data and combining it to a zipped tuple list    
    goal_list, assist_list, playerlist = [], [], []

    # converting the extracted data into lists
    for name in row1:  
        playerlist.append(name.text)

    for stat in row2:
        goal_list.append(stat.text)
        
    for stat in row3:
        assist_list.append(stat.text)

    goal_list = [re.sub(r"\W", "", stat) for stat in goal_list]  # eliminating whitespaces
    goal_list = [int(stat) for stat in goal_list]

    assist_list = [re.sub(r"\W", "", stat) for stat in assist_list]
    assist_list = [int(stat) for stat in assist_list]

    # iterating over the 3 lists and combining/zipping the data into a list of tuples
    # player_statlist[i] = (list1[i], list2[i], list3[i]), for better parsing later on 
    player_statlist = list(zip(playerlist, goal_list, assist_list))   
    player_statlist.sort()
    # player_statlist = sorted(player_statlist, key=lambda x: x[1], reverse=True)

    print(player_statlist)
    print("Player Data Sent to MySQL database!")
    return player_statlist


def check_ratings():  # scrapes and extracts data from the premier league wesbite

    page = requests.get(URL, headers=headers1)  # storing the data in variable

    soup = BeautifulSoup(page.content, 'html.parser')  # storing the parsed data in variable
    # soup = BeautifulSoup(page.content, "lxml")

    # finding, extracting data attributes through the respective html classes and ids
    namerow = soup.find_all(class_="top-player-stats__name gel-double-pica")
    goalsrow = soup.find_all(class_="top-player-stats__goals-scored-number")
    assistsrow = soup.find_all(class_="top-player-stats__assists-number gel-double-pica")

    return parse_and_return(namerow, goalsrow, assistsrow)


check_ratings()

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

