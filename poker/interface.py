from tkinter import *
from main_game import Poker

class InterfacePoker(Poker):
    def __init__(self, balance, starting_value):
        super().__init__(balance, starting_value)

        print(self.player.balance)
        print(self.starting_value)
        self.root = Tk()
        self.root.title("Poker")
        self.root.config(bg="green")
        self.root.geometry("1200x800")

        self.body()
        self.info_section()
        self.computer_hand_section()
        self.buttons_section()
        self.player_hand_section()
        self.table_section()

        self.root.mainloop()

    def body(self):
        title = Label(self.root, text="Poker Game", font=("Arial", 16), bg="green")
        title.pack(pady=5)

        self.info_frame = Frame(self.root, bg="green")
        self.info_frame.pack(pady=5)
        
        self.computer_hand_frame = LabelFrame(self.root, bg="green", text="Computer hand", font=("Arial", 12))
        self.computer_hand_frame.pack(pady=5)

        self.table_frame = LabelFrame(self.root, bg="green", text="Table", font=("Arial", 12))
        self.table_frame.pack(pady=5)

        self.player_hand_frame = LabelFrame(self.root, bg="green", text="Your hand", font=("Arial", 12))
        self.player_hand_frame.pack(pady=5)

        self.buttons_frame = Frame(self.root, bg="green")
        self.buttons_frame.pack(pady=5)

    def info_section(self):
        self.info_label = Label(self.info_frame, text="Place your bet", bg="green", font=("Arial", 12))
        self.info_label.grid(row=0, column=0)

        self.player_bet_label = Label(self.info_frame, text=f"Your bet: {self.player.current_bet}", bg="green", font=("Arial", 12))
        self.player_bet_label.grid(row=0, column=1, padx=5)

        self.computer_bet_label = Label(self.info_frame, text=f"Computer bet: {self.computer.current_bet}", bg="green", font=("Arial", 12))
        self.computer_bet_label.grid(row=0, column=2)

        self.player_balance_label = Label(self.info_frame, text=f"player balance: {self.player.balance}", bg="green", font=("Arial", 12))
        self.player_balance_label.grid(row=0, column=3, padx=5)

        self.balance_label = Label(self.info_frame, text=f"Computer balance: {self.computer.balance}", bg="green", font=("Arial", 12))
        self.balance_label.grid(row=0, column=4)

    def cards_section(self):
        self.computer_card_1 = Label(self.computer_hand_frame, bg="green", image="")
        self.computer_card_1.grid(row=0, column=0, padx=5)

        self.computer_card_2 = Label(self.computer_hand_frame, bg="green", image="")	
        self.computer_card_2.grid(row=0, column=1, padx=5)

        self.table_card_1 = Label(self.table_frame, bg="green", image="")
        self.table_card_1.grid(row=0, column=0, padx=5)

        self.table_card_2 = Label(self.table_frame, bg="green", image="")
        self.table_card_2.grid(row=0, column=1, padx=5)

        self.table_card_3 = Label(self.table_frame, bg="green", image="")
        self.table_card_3.grid(row=0, column=2, padx=5)

        self.table_card_4 = Label(self.table_frame, bg="green", image="")
        self.table_card_4.grid(row=0, column=3, padx=5)

        self.table_card_5 = Label(self.table_frame, bg="green", image="")
        self.table_card_5.grid(row=0, column=4, padx=5)
        
        self.player_card_1 = Label(self.player_hand_frame, bg="green", image="")
        self.player_card_1.grid(row=0, column=0, padx=5)

        self.player_card_2 = Label(self.player_hand_frame, bg="green", image="")
        self.player_card_2.grid(row=0, column=1, padx=5)


    def computer_hand_section(self, state = False):
        global image1, image2

        if state:
            hand = self.get_cards()
            self.computer.deal_cards(hand)

            image_name = f"{hand[0][0]}_of_{hand[0][1]}"
            image1 = self.resize(image_name)
            self.computer_card_1.config(image=image1)

            image_name = f"{hand[1][0]}_of_{hand[1][1]}"
            image2 = self.resize(image_name)
            self.computer_card_2.config(image=image2)

    def table_section(self, state = False, first = True, second = False):
        global image5, image6, image7, image8, image9

        if state:
            if first:
                hand = self.get_cards(3)
                self.add_to_table(hand)

                image_name = f"{hand[0][0]}_of_{hand[0][1]}"
                image5 = self.resize(image_name)
                self.table_card_1.config(image=image5)

                image_name = f"{hand[1][0]}_of_{hand[1][1]}"
                image6 = self.resize(image_name)
                self.table_card_2.config(image=image6)

                image_name = f"{hand[2][0]}_of_{hand[2][1]}"
                image7 = self.resize(image_name)
                self.table_card_3.config(image=image7)
            elif second:
                hand = self.get_cards(1)
                self.add_to_table(hand)

                image_name = f"{hand[0][0]}_of_{hand[0][1]}"
                image8 = self.resize(image_name)
                self.table_card_4.config(image=image8)

            else:
                hand = self.get_cards(1)
                self.add_to_table(hand)

                image_name = f"{hand[0][0]}_of_{hand[0][1]}"
                image9 = self.resize(image_name)
                self.table_card_5.config(image=image9)

    def player_hand_section(self, state=False):
        global image3, image4

        if state:
            hand = self.get_cards()
            self.player.deal_cards(hand)

            image_name = f"{hand[0][0]}_of_{hand[0][1]}"
            image3 = self.resize(image_name)
            self.player_card_1.config(image=image3)

            image_name = f"{hand[1][0]}_of_{hand[1][1]}"
            image4 = self.resize(image_name)
            self.player_card_2.config(image=image4)

    def buttons_section(self):
        self.start_game_button = Button(self.buttons_frame, text="Start game", font=("Arial", 12), command=self.start_game)
        self.start_game_button.grid(row=0, column=0, padx=5)

        self.next_round_button = Button(self.buttons_frame, text="Next round", font=("Arial", 12), command=self.next_round)
        self.next_round_button.grid(row=0, column=1, padx=5)

        self.fold_button = Button(self.buttons_frame, text="Fold", font=("Arial", 12), command=self.fold)
        self.fold_button.grid(row=0, column=2, padx=5)

        self.call_button = Button(self.buttons_frame, text="Call", font=("Arial", 12) , command=lambda: self.call_the_bet("player"))
        self.call_button.grid(row=0, column=3, padx=5)

        self.raise_button = Button(self.buttons_frame, text="Raise", font=("Arial", 12), command=lambda: self.raise_the_bet("player", int(self.raised_value.get())))
        self.raise_button.grid(row=0, column=4, padx=5, pady=3)

        self.raised_value = Entry(self.buttons_frame, font=("Arial", 12))
        self.raised_value.grid(row=1, column=4, padx=5)

        self.all_in_button = Button(self.buttons_frame, text="All in", font=("Arial", 12), command=lambda: self.all_in("player"))
        self.all_in_button.grid(row=0, column=5, padx=5)

    def start_game(self):
        self.reset()
        self.cards_section()
        self.player_hand_section(state=True)
        self.table_section(state=True)
        self.computer_hand_section(state=True)
        self.player.current_bet = self.starting_value
        self.player.balance -= self.player.current_bet
        self.computer.current_bet = 2*self.starting_value
        self.computer.balance -= self.computer.current_bet
        self.update_bets()
        self.next_round_button.config(state=NORMAL)
        self.start_game_button.config(state=DISABLED)
        self.conroll_buttons(NORMAL)

    def end_game(self, winner):
        if winner == "player":
            self.info_label.config(text="You won")
            self.player.balance += self.computer.current_bet + self.player.current_bet
            self.reset()
        elif winner == "computer":
            self.info_label.config(text="Computer won")
            self.computer.balance += self.computer.current_bet + self.player.current_bet
            self.reset()
        else:
            self.info_label.config(text="Draw")
            self.player.balance += self.computer.current_bet
            self.computer.balance += self.player.current_bet
            self.reset()
        self.start_game_button.config(state=NORMAL)
        self.next_round_button.config(state=DISABLED)
        self.update_bets()


    def update_bets(self):
        self.player_bet_label.config(text=f"Your bet: {self.player.current_bet}")
        self.computer_bet_label.config(text=f"Computer bet: {self.computer.current_bet}")
        self.balance_label.config(text=f"Computer balance: {self.computer.balance}")
        self.player_balance_label.config(text=f"player balance: {self.player.balance}")

    def clear_the_table(self):
        self.table_card_1.config(image=None)
        self.table_card_2.config(image=None)
        self.table_card_3.config(image=None)
        self.table_card_4.config(image=None)
        self.table_card_5.config(image=None)

    def next_round(self):
        if self.player.balance > 0 and self.computer.balance > 0:
            self.conroll_buttons(NORMAL)
            if len(self.table) == 3:
                self.table_section(state=True, first=False, second=True)
            elif len(self.table) == 4:
                self.table_section(state=True, first=False, second=False)
                self.next_round_button.config(text="result")
            elif len(self.table) == 5:
                self.end_game(self.result())
            else:
                self.start_game()

            self.start_game_button.config(state=DISABLED)
            self.next_round_button.config(state=DISABLED)
        else:
            self.info_label.config(text="Game over")
            self.start_game_button.config(state=DISABLED)
            self.next_round_button.config(state=DISABLED)

    def conroll_buttons(self, state):
        self.fold_button.config(state=state)
        self.call_button.config(state=state)
        self.raise_button.config(state=state)
        self.all_in_button.config(state=state)

    def fold(self, who = 3):
        self.winner += who
        if who == 1:
            self.info_label.config(text="Computer folded")
            self.end_game("player")
        else:
            self.end_game("computer")
        self.conroll_buttons(DISABLED)
        self.next_round_button.config(state=DISABLED)
        self.start_game_button.config(state=NORMAL)

    def call_the_bet(self, who):
        if who == "player":
            amount = self.calling(who)
            self.player_bet_label.config(text=f"Your bet: {amount}")
            self.computer_turn("call")
        else:
            amount = self.calling(who)
            self.computer_bet_label.config(text=f"Computer bet: {amount}")
            self.info_label.config(text="Computer called")
            self.update_bets()
            self.conroll_buttons(DISABLED)
            self.next_round_button.config(state=NORMAL)

    def raise_the_bet(self, who, raised_value):
        if who == "player":
            if raised_value <= self.player.balance and raised_value > self.computer.current_bet:
                amount = self.raising("player", raised_value)
                self.player_bet_label.config(text=f"Your bet: {amount}")
                self.computer_turn("raise")
            else:
                self.info_label.config(text="Please enter a valid raise value")
        else:
            amount = self.raising("computer", raised_value)
            self.computer_bet_label.config(text=f"Computer bet: {amount}")
            self.info_label.config(text="Computer raised")
            self.update_bets()
            self.conroll_buttons(DISABLED)
            self.next_round_button.config(state=NORMAL)

    def all_in(self, who):
        if who == "player":
            if self.player.balance > self.computer.current_bet:
                amount = self.all_in_function("player")
                self.player_bet_label.config(text=f"Your bet: {amount}")
                self.computer_turn("all in")
            else:
                self.player_bet_label.config(text=f"Your bet: 0")
        else:
            if self.computer.balance > self.player.current_bet:
                amount = self.all_in_function("computer")
                self.computer_bet_label.config(text=f"Computer bet: {amount}")
            else:
                self.computer_bet_label.config(text=f"Computer bet: 0")
            self.update_bets()
            self.conroll_buttons(DISABLED)
            self.next_round_button.config(state=NORMAL) 

    def computer_turn(self, previous):
        evaluation = self.evaluation()

        if evaluation == "strong":
            decision = self.strong(previous)
        elif evaluation == "medium":
            decision = self.medium(previous)
        else:
            decision = self.weak(previous)

        if decision[0] == "fold":
            self.fold(who = 2)
            self.info_label.config(text="Computer folded")
        elif decision[0] == "call":
            self.call_the_bet("computer")
            self.info_label.config(text="Computer called")
        elif decision[0] == "raise":
            self.raise_the_bet("computer", decision[1])
            self.info_label.config(text="Computer raised")
        elif decision[0] == "all in":
            self.all_in("computer")
            self.info_label.config(text="Computer all in")