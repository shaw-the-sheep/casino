from tkinter import *
from main_game import Poker
from interface import InterfacePoker
class StartingPage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Poker")
        self.root.geometry("600x300")

        self.title = Label(self.root, text="Poker Game", font=("Arial", 16))
        self.title.pack(pady=5)

        self.input_frame = Frame(self.root)
        self.input_frame.pack(pady=5)

        self.name = "player1"
        self.balance = 150000000000

        self.playing_balance_label = Label(self.input_frame, text="Balance:")
        self.playing_balance_label.grid(row=1, column=0)

        self.playing_balance_entry = Entry(self.input_frame)
        self.playing_balance_entry.grid(row=1, column=1)

        self.info_label = Label(self.root, text="choose the amount of money you will play with", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.start_bet_frame = LabelFrame(self.root, text="choose the amout of money the first 2 rounds will start with", font=("Arial", 12))
        self.start_bet_frame.pack(pady=5)
        
        self.radio_buttons()

        self.start_button = Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=5)

        self.root.mainloop()

    def radio_buttons(self):
        self.start_money = DoubleVar()

        self.five_perc_button = Radiobutton(self.start_bet_frame, text="5%", variable=self.start_money, value=5/100)
        self.five_perc_button.grid(row=0, column=0)

        self.ten_perc_button = Radiobutton(self.start_bet_frame, text="10%", variable=self.start_money, value=10/100)
        self.ten_perc_button.grid(row=0, column=1)

        self.fifteen_perc_button = Radiobutton(self.start_bet_frame, text="15%", variable=self.start_money, value=15/100)
        self.fifteen_perc_button.grid(row=0, column=2)

        self.twenty_perc_button = Radiobutton(self.start_bet_frame, text="20%", variable=self.start_money, value=20/100)
        self.twenty_perc_button.grid(row=0, column=3)

    def start_game(self):
        if self.playing_balance_entry.get().isdigit():
            if self.balance >= int(self.playing_balance_entry.get()):
                money = int(self.playing_balance_entry.get())
                starting_value = int(self.start_money.get() * money)
                if starting_value == 0:
                    starting_value = 5/100 * money
                self.root.destroy()
                InterfacePoker(money, starting_value)
            else:
                self.info_label.config(text="You don't have enough money")
        else:
            self.info_label.config(text="Please enter a valid number")


StartingPage()