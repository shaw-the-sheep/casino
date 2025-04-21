from tkinter import *
from roulette import Game
class InterfaceRoulette(Game):
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("Roulette")
        self.root.config(bg="green")
        self.root.geometry("1200x800")

        self.body()
        self.bet_section()
        self.button_section()
        self.table()
        self.navigation_section()

        self.root.mainloop()

    def body(self):
        title = Label(self.root, text="Roulette Game", font=("Arial", 16), bg="green")
        title.pack(pady=5)

        self.bet_frame = LabelFrame(self.root, text="Your bet and balance:", bg="green", font=("Arial", 12))
        self.bet_frame.pack(pady=5) 

        self.info = Label(self.root, text="Place your bet", bg="green", font=("Arial", 12))
        self.info.pack(pady=5)

        self.buttons_frame = LabelFrame(self.root, text="choose type of bet", bg="green", font=("Arial", 12))
        self.buttons_frame.pack(pady=5)

        self.table_frame = Frame(self.root)
        self.table_frame.pack(pady=5)

        self.navigation_frame = Frame(self.root, bg="green")
        self.navigation_frame.pack(pady=5)

    def bet_section(self):
        bet_label = Label(self.bet_frame, text="Your bet:", bg="green", font=("Arial", 12))
        bet_label.grid(row=0, column=0, padx=5, pady=3)

        self.bet_entery = Entry(self.bet_frame, font=("Arial", 12))
        self.bet_entery.grid(row=0, column=1, pady=3)

        balance_label = Label(self.bet_frame, text="Your balance:", bg="green", font=("Arial", 12))
        balance_label.grid(row=0, column=2, padx=5, pady=3)

        self.balance_show = Label(self.bet_frame, text=str(self.balance), bg="green", font=("Arial", 12))
        self.balance_show.grid(row=0, column=3, pady=3)

        self.throw_button = Button(self.bet_frame, text="Throw the ball", font=("Arial", 12), command=lambda: self.throw_ball(self.info, self.inside_bet_value.get(), 
                                                                                                            self.balance_show, self.throw_button, self.bet_entery.get(), 
                                                                                                            self.ball_value))
        self.throw_button.grid(row=0, column=4, padx=5, pady=3)

        self.ball_value = Label(self.bet_frame, text="", bg="green", font=("Arial", 12))
        self.ball_value.grid(row=0, column=5, pady=3)

    def selection(self):
        self.selected_bet = self.choice.get()
        self.info.config(text=f"You selected {self.selected_bet}")

    def button_section(self):
        self.choice = StringVar()

        # inside bet
        self.inside_bet = Radiobutton(self.buttons_frame, text="choose one number: ", variable=self.choice, value="inside", font=("Arial", 12), bg="green", command=self.selection)
        self.inside_bet.grid(row=0, column=0, padx=5, pady=5)

        self.inside_bet_value = Entry(self.buttons_frame, font=("Arial", 12))
        self.inside_bet_value.grid(row=1, column=0, padx=5)

        #odd even
        self.odd_button = Radiobutton(self.buttons_frame, text="odd", variable=self.choice, font=("Arial", 12), bg="green", value="odd", command=self.selection)
        self.odd_button.grid(row=0, column=1, pady=5)

        self.even_button = Radiobutton(self.buttons_frame, text="even", variable=self.choice, font=("Arial", 12),   bg="green", value="even",   command=self.selection)                             
        self.even_button.grid(row=1, column=1)

        # red black
        self.red_button = Radiobutton(self.buttons_frame, text="red", variable=self.choice, font=("Arial", 12), bg="green", value="red", command=self.selection)
        self.red_button.grid(row=0, column=2, pady=5)

        self.black_button = Radiobutton(self.buttons_frame, text="black", variable=self.choice, font=("Arial", 12), bg="green", value="black", command=self.selection)
        self.black_button.grid(row=1, column=2)

        # low high
        self.low_button = Radiobutton(self.buttons_frame, text="low", variable=self.choice, font=("Arial", 12), bg="green", value="low", command=self.selection)
        self.low_button.grid(row=0, column=3, pady=5)

        self.hight_button = Radiobutton(self.buttons_frame, text="hight", variable=self.choice, font=("Arial", 12), bg="green", value="hight", command=self.selection)  
        self.hight_button.grid(row=1, column=3)

    def table(self):

        i = 0
        column = 0
        while i < (len(self.roulette_numbers)):
            for j in range(3):
                if self.roulette_numbers[i][1] == 'red':
                    label = Label(self.table_frame, text=str(self.roulette_numbers[i][0]), font=("Arial", 12), bg="red", height=5, width=10)
                else:
                    label = Label(self.table_frame, text=str(self.roulette_numbers[i][0]), font=("Arial", 12), bg="black", fg="white", height=5, width=10)
                label.grid(row=j, column=column)
                i += 1
            column += 1

    def navigation_section(self):
        self.restart_button = Button(self.navigation_frame, text="Restart", font=("Arial", 12), command=self.retart_the_game)
        self.restart_button.grid(row=0, column=0, padx=5, pady=5)


    
    def retart_the_game(self):
        self.bet = 0
        self.selected_bet = ""
        self.ball = None
        self.ratio = 1
        self.bet_entery.delete(0, END)
        self.info.config(text="Place your bet")
        self.ball_value.config(text="")

InterfaceRoulette()