from python_files.cards import Cards

class Player:
    def __init__(self, name: str, balance = 1.0):

        assert balance > 0
        assert name.isalpha() 

        self.balance = balance
        self.name = name
        self.points = 0
        self.hand = []
        self.bet = 0

    def calculate_balance(self, x, sign):
        if sign == "+":
            self.balance += x
        elif sign == "-":
            self.balance -= x
                    
    def add_bet(self, x):
        if x > self.balance:
            return "You don't have enough money"
        else:
            self.bet = x
            self.calculate_balance( x , "-")
            return f"Balance: {self.balance}"
        
    def winning_bet(self, rate):
        winning = self.bet * rate
        self.calculate_balance(winning, "+")
    
    def play(self):
        card = Cards()
        self.hand.append(card.dealing(self.name, 1)[0])
        print(f"{self.name} got {self.hand[-1][0]} {self.hand[-1][1]}")
        self.points = card.total(self.hand)
        print(f"{self.name} total is {self. points}")
        