from tkinter import *
from python_files.cards import Cards
from python_files.player import Player
import time

# instances
class Interface:
    def __init__(self):
        self.card = Cards()

        self.login()

    # name page
    def login(self):
        self.login_win = Tk()
        self.login_win.title("Blackjack")
        self.login_win.geometry("400x300")
        self.login_win.configure(bg="green")
        icon = PhotoImage(file="cards_img/game.png")  # Replace with your icon path
        self.login_win.iconphoto(False, icon)

        self.create_player_frame = Frame(self.login_win, bg="green")
        self.create_player_frame.pack(pady=20)

        self.name_label = Label(self.create_player_frame, text="Name: ", font=("Arial", 14), bg="green")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)

        self.name_entry = Entry(self.create_player_frame, font=("Arial", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        balance_label = Label(self.create_player_frame, text="Balance: ", font=("Arial", 14), bg="green")
        balance_label.grid(row=1, column=0, padx=10, pady=5)

        self.balance_entry = Entry(self.create_player_frame, font=("Arial", 14))
        self.balance_entry.grid(row=1, column=1, padx=10, pady=5)

        self.create_button = Button(self.create_player_frame, text="Create", font=("Arial", 14), padx=20, pady=10, command=self.players)
        self.create_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.status_label = Label(self.create_player_frame, text="", font=("Arial", 14), bg="green")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=10)

        # creating players

        self.login_win.mainloop()
    
    def players(self):
        try:
            self.p1 = Player(self.name_entry.get(), int(self.balance_entry.get()))
            self.p2 = Player("dealer")

            self.start_game(self.login_win)           
        except ValueError:
            self.status_label.config(text="Invalid input. Please try again.")
        except AssertionError as e:
            self.status_label.config(text="Invalid input. Please try again.")

    def start_game(self, previous):
        # setting up main window
        previous.destroy()

        self.init_balance = self.p1.balance

        self.root = Tk()

        self.root.title("Blackjack")
        icon = PhotoImage(file="cards_img/game.png")  # Replace with your icon path
        self.root.iconphoto(False, icon)
        self.root.geometry("1200x800")
        self.root.title("Interface")
        self.root.configure(bg="green")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # creating frame
        self.my_frame = Frame(self.root, bg="green")
        self.my_frame.grid(row=0, column=0, sticky="nsew", ipady=10)

        self.my_frame.grid_rowconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        
        self.button_frame = Frame(self.root, bd=0, bg="green")
        self.button_frame.grid(row=1, column=0, ipady=10 )

        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Frames for cards
        self.dealer_frame = LabelFrame(self.my_frame, text = "Dealer", bd = 0, font=("Arial", 14), labelanchor="n")
        self.dealer_frame.grid(row=0, column=0, padx=10, ipadx=10, pady=5)

        self.player_frame = LabelFrame(self.my_frame, text=self.p1.name, bd=0, font=("Arial", 14), labelanchor="n")
        self.player_frame.grid(row=1, column=0, padx=20, ipadx=10)

        self.score_frame = LabelFrame(self.my_frame, text="Score", bd=0, font=("Arial", 14), labelanchor="n")
        self.score_frame.grid(row=2, column=0, columnspan=2, pady=20, ipadx=20)
      
        # buttons

        self.info_frame = LabelFrame(self.button_frame, text="Info", bd=0, font=("Arial", 14), bg="green", labelanchor="n")
        self.info_frame.grid(row=0, column=0)

        self.shuffle_button = Button(self.button_frame, text="Restart", font=("Arial", 14), padx=20, pady=10, command=self.new)   
        self.shuffle_button.grid(row=0, column=1, pady=10, padx=20)

        self.bet_button = Button(self.button_frame, text="Bet", font=("Arial", 14), padx=20, pady=10, command=self.bet)
        self.bet_button.grid(row=0, column=2, pady=10, padx=20)

        self.deal_button = Button(self.button_frame, text="Hit me", font=("Arial", 14), padx=20, pady=10, command=self.deal_players, state="disabled")
        self.deal_button.grid(row=0, column=3, pady=10, padx=20) 

        self.stand_button = Button(self.button_frame, text="Stand", font=("Arial", 14), padx=20, pady=10, command=self.dealer_turn, state="disabled")
        self.stand_button.grid(row=0, column=4, pady=10, padx=20)

        self.current_balanceframe = LabelFrame(self.button_frame, text="your balance is :", font=("Arial", 14))
        self.current_balanceframe.grid(row=0, column=5, pady=10)

        # put cards in frames

        # cards for dealer
        # 1
        self.dealer_label_1 = Label(self.dealer_frame, text="")
        self.dealer_label_1.grid(row=0, column=0, pady=0, padx=5)

        # 2
        self.dealer_label_2 = Label(self.dealer_frame, text="")
        self.dealer_label_2.grid(row=0, column=1, pady=0, padx=5)

        # 3
        self.dealer_label_3 = Label(self.dealer_frame, text="")
        self.dealer_label_3.grid(row=0, column=2, pady=0, padx=5)

        # 4    
        self.dealer_label_4 = Label(self.dealer_frame, text="")
        self.dealer_label_4.grid(row=0, column=3, pady=0, padx=5)

        # 5
        self.dealer_label_5 = Label(self.dealer_frame, text="")
        self.dealer_label_5.grid(row=0, column=4, pady=0, padx=5)

        # cards for player
        # 1
        self.player_label_1 = Label(self.player_frame, text="")
        self.player_label_1.grid(row=0, column=0, pady=10, padx=5)

        # 2
        self.player_label_2 = Label(self.player_frame, text="")
        self.player_label_2.grid(row=0, column=1, pady=10, padx=5)

        # 3
        self.player_label_3 = Label(self.player_frame, text="")
        self.player_label_3.grid(row=0, column=2, pady=10, padx=5)

        # 4
        self.player_label_4 = Label(self.player_frame, text="")
        self.player_label_4.grid(row=0, column=3, pady=10, padx=5)

        # 5
        self.player_label_5 = Label(self.player_frame, text="")
        self.player_label_5.grid(row=0, column=4, pady=10, padx=5)

        self.info_label = Label(self.info_frame, text="", font=("Arial", 14), fg="red", bg="green")
        self.info_label.pack(pady=10)

        self.player_score_label = Label(self.score_frame, text="", font=("Arial", 14))
        self.player_score_label.grid(row=0, column=1, pady=20, padx=50)

        self.dealer_score_label = Label(self.score_frame, text="", font=("Arial", 14))
        self.dealer_score_label.grid(row=0, column=0, pady=20, padx=50)

        self.balance_label = Label(self.current_balanceframe, text="", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.new()
        self.update_balance()





        self.root.mainloop()


    def new(self):
        self.info_label.config(text="Shuffling...")
        self.card.creat_cards()
        self.info_frame.after(1000, lambda: self.info_label.config(text=""))

        self.pointer_player = 1
        self.pointer_dealer = 1

        self.p1.hand = []
        self.p2.hand = []

        self.p1.points = 0
        self.p2.points = 0

        self.player_score_label.config(text=f"{self.p1.points}")
        self.dealer_score_label.config(text=f"{self.p2.points}")

        self.update_balance()
        self.deal_button.config(state="disabled")
        self.stand_button.config(state="disabled")
        self.bet_button.config(state="normal")

        self.player_label_1.config(image="")
        self.player_label_2.config(image="")
        self.player_label_3.config(image="")
        self.player_label_4.config(image="")
        self.player_label_5.config(image="")

        self.dealer_label_1.config(image="")
        self.dealer_label_2.config(image="")
        self.dealer_label_3.config(image="")        
        self.dealer_label_4.config(image="")
        self.dealer_label_5.config(image="")

        global player_image
        player_image = ""

        global dealer_image
        dealer_image = ""

        dealer_image = self.card.resize("back")
        self.dealer_label_1.config(image=dealer_image)

        player_image = self.card.resize("back")
        self.player_label_1.config(image=player_image) 

    # Functions
    def deal_players(self, nb = 1):
        p = self.card.dealing(self.p1, nb)

        global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5

        if self.pointer_player == 1:
            player_image_1 = self.card.resize(p[0])
            self.player_label_1.config(image=player_image_1) 

            player_image_2 = self.card.resize(p[1])
            self.player_label_2.config(image=player_image_2)

            self.pointer_player += 2

        elif self.pointer_player== 3:
            player_image_3 = self.card.resize(p[0])
            self.player_label_3.config(image=player_image_3)

            self.pointer_player += 1

        elif self.pointer_player == 4:
            player_image_4 = self.card.resize(p[0])
            self.player_label_4.config(image=player_image_4)

            self.pointer_player += 1

        elif self.pointer_player == 5:
            player_image_5 = self.card.resize(p[0])
            self.player_label_5.config(image=player_image_5)
        
            self.pointer_player += 1
        
        else:
            self.info_label.config(text="You win!")
            self.p1.winning_bet(2)
            self.update_balance

        self.p1.points = self.card.total(self.p1.hand)
        self.player_score_label.config(text=f"{self.p1.points}")

        if self.p1.points >= 21:
            self.stand()

    def deal_dealer(self, nb = 1):
        d = self.card.dealing(self.p2, nb)

        global dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5

        if self.pointer_dealer == 1:
            dealer_image_1 = self.card.resize(d[0])
            self.dealer_label_1.config(image=dealer_image_1)

            dealer_image_2 = self.card.resize(d[1])
            self.dealer_label_2.config(image=dealer_image_2)

            self.pointer_dealer += 2

        elif self.pointer_dealer == 3:
            dealer_image_3 = self.card.resize(d[-1])
            self.dealer_label_3.config(image=dealer_image_3)

            self.pointer_dealer += 1

        elif self.pointer_dealer == 4:
            dealer_image_4 = self.card.resize(d[-1])
            self.dealer_label_4.config(image=dealer_image_4)

            self.pointer_dealer += 1

        elif len(d) == 5:
            dealer_image_5 = self.card.resize(d[-1])
            self.dealer_label_5.config(image=dealer_image_5)   

            self.pointer_dealer += 1

        self.p2.points = self.card.total(self.p2.hand)
        self.dealer_score_label.config(text=f"{self.p2.points}") 

    def dealer_turn(self):
        self.deal_dealer(2)
        if self.p2.points < 17:
            self.root.after(2000, lambda:self.deal_dealer())
        self.root.after(3000, lambda:self.stand())

    def stand(self):
        if self.p1.points == 21 and self.p2.points != 21:
            self.info_label.config(text="Blackjack! You win!")
            ratio = 3
            self.p1.winning_bet(ratio)
        else:
            if self.p2.points == 21 and self.p1.points != 21:
                self.info_label.config(text=f"{self.p2.name} has a Blackjack!")
                ratio = -0.5
                self.p1.winning_bet(ratio)
            elif self.p1.points > 21 and self.p2.points < 21:
                self.info_label.config(text=f"{self.p1.name} busted. {self.p2.name} wins!")
            elif self.p2.points > 21 and self.p1.points < 21:
                self.info_label.config(text=f"{self.p2.name} busted. {self.p1.name} wins!")
                ratio = 1.5
                self.p1.winning_bet(ratio)
            elif self.p1.points > self.p2.points:
                self.info_label.config(text=f"{self.p1.name} wins!")
                ratio = 2
                self.p1.winning_bet(ratio)
            elif self.p2.points > self.p1.points:
                self.info_label.config(text=f"{self.p2.name} wins!")
            else:
                self.info_label.config(text="It's a tie!")
                ratio = 1
                self.p1.winning_bet(self.bet, ratio)

        self.info_frame.after(5000, lambda: self.info_label.config(text=""))

        if self.p1.balance <= 0:
            self.info_label.config(text="You ran out of money. Game over.")
            self.info_frame.after(4000, lambda: self.info_label.config(text=""))

            self.root.after(5000, lambda: exit())

        self.root.after(5000, lambda: self.new())

    def bet(self):
        self.bet_win = Tk()
        self.bet_win.title("Blackjack")
        self.bet_win.geometry("400x300")
        self.bet_win.configure(bg="green")

        self.create_bet_frame = Frame(self.bet_win, bg="green")
        self.create_bet_frame.pack(pady=20)

        self.bet_label = Label(self.create_bet_frame, text="Place your bet: ", font=("Arial", 14), bg="green")
        self.bet_label.grid(row=0, column=0, padx=10, pady=5)

        self.bet_entry = Entry(self.create_bet_frame, font=("Arial", 14))
        self.bet_entry.grid(row=0, column=1, padx=10, pady=5)

        balance_label = Label(self.create_bet_frame, text="Balance: ", font=("Arial", 14), bg="green")
        balance_label.grid(row=1, column=0, padx=10, pady=5)

        self.balance_value = Label(self.create_bet_frame, text=f"{self.p1.balance}", font=("Arial", 14), background="green", anchor="w")
        self.balance_value.grid(row=1, column=1, padx=10, pady=5)

        self.confirm_button = Button(self.create_bet_frame, text="Create", font=("Arial", 14), padx=20, pady=10, command=lambda: self.confirming_bet(self.bet_entry.get()))
        self.confirm_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.status_label = Label(self.create_bet_frame, text="", font=("Arial", 14), bg="green")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.bet_win.mainloop()

    def confirming_bet(self, bet: float):
        try:
            answer = self.p1.add_bet(float(bet))

            if answer == "You don't have enough money":
                self.status_label.config(text=answer)
            else:            
                self.bet_win.destroy()
                self.update_balance()
                self.deal_players(2)
                self.deal_button.config(state="normal")
                self.stand_button.config(state="normal")
                self.bet_button.config(state="disabled")

        except ValueError:
            self.status_label.config(text="Invalid input. Please try again.")


    def update_balance(self):
        self.balance_label.config(text=f"{self.p1.balance}")

Interface()