from random import sample
class Game:
    def __init__(self):
        self.bet = 0
        self.balance = 1000
        self.selected_bet = ""
        self.ball = None
        self.ratio = 1

        self.roulette_numbers = self.numbers()

    def numbers(self):
        return [
        (1, 'red'), (2, 'black'), (3, 'red'), 
        (4, 'black'), (5, 'red'), (6, 'black'), 
        (7, 'red'), (8, 'black'), (9, 'red'), 
        (10, 'black'), (11, 'black'), (12, 'red'), 
        (13, 'black'), (14, 'red'), (15, 'black'), 
        (16, 'red'), (17, 'black'), (18, 'red'), 
        (19, 'red'), (20, 'black'), (21, 'red'),
        (22, 'black'), (23, 'red'), (24, 'black'), 
        (25, 'red'), (26, 'black'), (27, 'red'), 
        (28, 'black'), (29, 'black'), (30, 'red'), 
        (31, 'black'), (32, 'red'), (33, 'black'), 
        (34, 'red'), (35, 'black'), (36, 'red')
        ]
    
    def get_the_bet(self, bet_entry, label):
        self.bet = bet_entry
        if self.bet.isdigit() is False:
            label.config(text="Please enter a valid bet")
            return False
        elif int(self.bet) > self.balance:
            label.config(text="You don't have enough money")
            return False
        if self.selected_bet == "":
            label.config(text="Please select a bet")
            return False
        self.balance -= int(self.bet)
        return True

    def throw_ball(self, label, inside_entry, balance_label, throw_button, bet_entry, ball_label):
        if self.get_the_bet(bet_entry, label) and self.inside_verification(inside_entry):
            self.ball = sample(self.roulette_numbers, 1)[0]
            ball_label.config(text=f"The ball landed on {self.ball[0]} {self.ball[1]}")
            result = self.result_verification(label, inside_entry)
            self.show_result(label, result)
            self.update_balance(balance_label, throw_button)
        else:
            label.config(text="Somthing is wrong, please try again")

    def inside_verification(self, entry):
        if not("0" <= entry <= "36") and self.selected_bet == "inside":
            return False
        return True
    
    def result_verification(self, label, inside_entry):
        if self.selected_bet == "inside":
            self.ratio = 35
            return self.ball[0] == int(inside_entry)
            
        elif self.selected_bet == "odd":
            self.ratio = 2
            return self.ball[0] % 2 == 1
        
        elif self.selected_bet == "even":
            self.ratio = 2
            return self.ball[0] % 2 == 0
        
        elif self.selected_bet == "low":
            self.ratio = 2
            return self.ball[0] < 19
        
        elif self.selected_bet == "hight":
            self.ratio = 2
            return self.ball[0] > 18
        
        elif self.selected_bet == "red":
            self.ratio = 2
            return self.ball[1] == "red"
        
        elif self.selected_bet == "black":
            self.ratio = 2
            return self.ball[1] == "black"
        
        else:
            label.config(text="Please choose a valid bet")
            return None
        
    def show_result(self, label, result):
        if result:
            label.config(text=f"You won!")
            self.balance += int(self.bet) * self.ratio
        elif result is False:
            label.config(text="You lost!")

    def update_balance(self, label, button):
        label.config(text=f"{self.balance}")
        if self.balance <= 0:
            label.config(text="You lost all your money!")
            button.config(state="disabled")

Game()