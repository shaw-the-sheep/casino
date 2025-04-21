from tkinter import *
from sqlite3 import connect

class Credentials:
    def __init__(self, master, username, password):
        self.username = username

    def what_to_do(self):
        if len(self.get_player()) == 0:
            self.add_player(0)
            self.player = self.get_player()[0]
        else:
            self.player = self.get_player()[0] 

    def get_player(self):
        db = connect("players.db")
        cursor = db.cursor()
        cursor.execute("SELECT balance FROM players WHERE username = ?", (self.username,))
        result = cursor.fetchone()
        db.close()
        return result
    
    def add_player(self):
        db = connect("players.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO players (username, balance) VALUES (?, ?)", (self.username, 0))
        db.commit()
        db.close()

    def update_balance(self, balance):
        db = connect("players.db")
        cursor = db.cursor()
        cursor.execute("UPDATE players SET balance = ? WHERE username = ?", (balance, self.username))
        db.commit()
        db.close()


# create the table players
db = connect("players.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS players (
    username TEXT,
    balance INTEGER
)""")
db.commit()
db.close()