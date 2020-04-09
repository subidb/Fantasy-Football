#classes, functions and  decorators for appUser, PointsTable, and PlayersStats

class AppUser:
    def __init__(self, id_num, username, email, passwd, money):
        self.id_num = id_num
        self.username = username
        self.email = email
        self.passwd = passwd
        self.money = money

    def __repr__(self):
        return "[Userid: {}, username: {} email: {} password: {} money: {}]".\
            format(self.id_num, self.username, self.email, self.passwd, self.money)


class UserPoints:
    def __init_(self, userid, week1, week2, week3, total):
        self.userid = userid
        self.week1 = week1
        self.week2 = week2
        self.week3 = week3

    @property
    def total_points(self):
        return self.week1 + self.week2 + self.week3



class Player:
    def __init__(self, player_id, name, position, goals, assists, numof_users, rating):
        self.player_id = player_id
        self.name = name
        self.position = position
        self.goals = goals
        self.assists = assists
        self.numof_users = numof_users
        self.rating = rating

    def __repr__(self):
        return 

    @property
    def value(self):
        return self.rating + (self.numof_users/10)

    @property
    def points(self):
        return self.goals * 4 + self.assists * 3 + self.rating






