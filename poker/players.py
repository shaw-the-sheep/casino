
class Player:
    def __init__(self, balance):
        self.balance = balance

        self.hand = []
        self.current_bet = 0
        self.previous_play = ""

    def deal_cards(self, cards):
        for card in cards:
            self.hand.append(card)

    def loosing(self, amoount):
        self.balance -= amoount

    def winning(self, amoount):
        self.balance += amoount

    def update_balance(self):
        return self.balance

class Computer:
    def __init__(self, balance):        
        self.hand = []
        self.accumulated_bet = 0

        self.balance = balance

        self.current_bet = 0
    
    def deal_cards(self, cards):
        for card in cards:
            self.hand.append(card)

    def loosing(self, amoount):
        self.balance -= amoount

    def winning(self, amoount):
        self.balance += amoount

    def update_balance(self):
        return self.balance
    