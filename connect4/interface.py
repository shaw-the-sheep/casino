from tkinter import *
from connect4 import Connect4


class InterfaceConnect4(Connect4):
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("Connect 4")
        self.root.geometry("600x600")

        self.body()
        self.info_section()
        self.button_section()
        self.grid_section()

        self.root.mainloop()

    def body(self):

        title = Label(self.root, text="Connect 4", font=("Arial", 16))
        title.pack(pady=5)
        
        self.info_frame = Frame(self.root)
        self.info_frame.pack(pady=5)

        self.grid_frame = Frame(self.root)
        self.grid_frame.pack(pady=5)

    def info_section(self):
        self.balance_label = Label(self.info_frame, text="Balance: ", font=("Arial", 14))
        self.balance_label.grid(row=0, column=0, padx=10, pady=5)

        self.balance_value = Label(self.info_frame, text=f"{self.balance}", font=("Arial", 14), anchor="w")
        self.balance_value.grid(row=0, column=1, padx=10, pady=5)

        self.winnig_times_label = Label(self.info_frame, text="Winning times: ", font=("Arial", 14))
        self.winnig_times_label.grid(row=0, column=2, padx=10, pady=5)

        self.winnig_times_value = Label(self.info_frame, text=f"{self.winning_times}", font=("Arial", 14), anchor="w")
        self.winnig_times_value.grid(row=0, column=3, padx=10, pady=5)

        self.restart_button = Button(self.info_frame, text="Restart", font=("Arial", 12), command=self.restart_the_game)
        self.restart_button.grid(row=0, column=4, padx=5, pady=5)

    def button_section(self):
        self.column1_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(0,
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column1_button.grid(row=0, column=0)

        self.column2_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(1, 
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column2_button.grid(row=0, column=1)

        self.column3_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(2, 
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column3_button.grid(row=0, column=2)

        self.column4_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(3, 
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column4_button.grid(row=0, column=3)

        self.column5_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(4, 
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column5_button.grid(row=0, column=4)

        self.column6_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(5, 
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column6_button.grid(row=0, column=5)

        self.column7_button = Button(self.grid_frame, text="--", font=("Arial", 12), bg="black", fg = "white", width=5, command=lambda: self.domove(6, 
                                                                                                        self.grid_frame, self.restart_the_game, 
                                                                                                        self.update_balance_winning_times))
        self.column7_button.grid(row=0, column=6)

    def grid_section(self):
        labels = [Label(self.grid_frame, bg="white", bd=1, relief="solid", width=10, height=2) for _ in range(42)]
        k = 0
        for i in range(1, 7):
            for j in range(7):
                labels[k].grid(row=i, column=j)
                k += 1

    def restart_the_game(self):
        self.grid_section()
        self.columns_count = [0]*7
        self.grid = [[" " for i in range(7)] for j in range(6)]

    def update_balance_winning_times(self):
        self.balance_value.config(text=f"{self.balance}")
        self.winnig_times_value.config(text=f"{self.winning_times}")

InterfaceConnect4()