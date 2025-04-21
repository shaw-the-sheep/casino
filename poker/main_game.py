from random import sample
from PIL import ImageTk, Image
from players import Player, Computer
from random import random as rd
from random import randint


class Poker:
    def __init__(self, balance, starting_value):
        self.player = Player(balance)
        self.computer = Computer(balance)

        self.starting_value = starting_value
        self.reset()
        self.table = []

        self.winner = -1
        self.test = False

    def reset(self):
        self.player.current_bet = 0
        self.computer.current_bet = 0
        self.winner = -1
        self.deck = self.deck_of_cards()

    def deck_of_cards(self):
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["hearts", "diamonds", "clubs", "spades"]

        deck = [(number, suit) for number in numbers for suit in suits]
        return deck
    
    def get_cards(self, nb = 2):
        cards = sample(self.deck, nb)

        for card in cards:
            self.deck.remove(card)

        return cards
    
    def resize(self, card):
        image = Image.open(f"poker/cards_img/{card}.png")
        new_width = 100
        aspect_ratio = image.width / image.height
        new_height = int(new_width / aspect_ratio)
        new_image = image.resize((new_width, new_height))
        return ImageTk.PhotoImage(new_image)
    
    def add_to_table(self, cards):
        for card in cards:
            self.table.append(card)

    def calling(self, who):
        if who == "player":
            self.player.balance = self.player.balance + self.player.current_bet - self.computer.current_bet
            self.player.current_bet = self.computer.current_bet
            return self.player.current_bet
        elif who == "computer":
            self.computer.balance = self.computer.balance + self.computer.current_bet - self.player.current_bet
            self.computer.current_bet = self.player.current_bet
            return self.computer.current_bet
        
    def raising(self, who, raised_value):
        if who == "player":
            self.player.balance -= raised_value
            self.player.current_bet += raised_value
            return self.player.current_bet
        elif who == "computer":
            self.computer.balance -= raised_value
            self.computer.current_bet += raised_value
            return self.computer.current_bet
        
    def all_in_function(self, who):
        if who == "player":
            self.player.current_bet += self.player.balance
            self.player.balance = 0
        else:
            self.computer.current_bet += self.computer.balance
            self.computer.balance = 0
        return 0
    
    def Hand_ranking(self, who_cards):
        if self.is_royal_flush(who_cards):
            return 10
        elif self.is_straight_flush(who_cards):
            return 9
        elif self.is_four_of_a_kind(who_cards):
            return 8
        elif self.is_full_house(who_cards):
            return 7
        elif self.is_flush(who_cards):
            return 6
        elif self.is_straight(who_cards):
            return 5
        elif self.is_three_of_a_kind(who_cards):
            return 4
        elif self.is_two_pair(who_cards):
            return 3
        elif self.is_pair(who_cards):
            return 2
        else:
            return 1
        
    def result(self):
        p = self.Hand_ranking(self.player.hand)
        c = self.Hand_ranking(self.computer.hand)
        if p > c:
            return "player"
        elif p < c:
            return "computer"
        else:
            return "tie"
        
    def is_royal_flush(self, who_cards):
        all_cards = self.table + who_cards
        numbers = ["A", "K", "Q", "J", "10"]
        suits = ["hearts", "diamonds", "clubs", "spades"]

        royal_flush = [[(number, suit) for number in numbers] for suit in suits]

        for cards in royal_flush:
            if all(card in all_cards for card in cards):
                return True

        return False

    def is_straight_flush(self, who_cards):
        all_cards = self.table + who_cards
        
        all_cards.sort(key=lambda x: self.custom_key(x))
        
        result = []
        start_suit = all_cards[0][1]
        start_number = self.custom_key(all_cards[0][0])
        result.append(all_cards[0])

        for i in range(1, len(all_cards)):
            print(len(result))
            if len(result) == 5:
                break
            if all_cards[i][1] == start_suit and self.custom_key(all_cards[i][0]) == start_number + 1:
                print("append")
                result.append(all_cards[i])
                start_number = self.custom_key(all_cards[i][0]) 
            else:
                result.clear()
                result.append(all_cards[i])
                start_suit = all_cards[i][1]
                start_number = self.custom_key(all_cards[i][0])
        
        return len(result) == 5


    def is_four_of_a_kind(self, who_cards):
        all_cards = self.table + who_cards
        start_number = all_cards[0][0]
        result = []
        all_cards.sort(key=lambda x: x[0])

        for i in range(1, len(all_cards)):
            if len(result) == 4:
                break

            if all_cards[i][0] == start_number:
                result.append(all_cards[i])
            else:
                start_number = all_cards[i][0]
                result.clear()
                result.append(all_cards[i])
        
        return len(result) == 4

    def is_full_house(self, who_cards):
        if self.is_three_of_a_kind(who_cards) and self.is_pair(who_cards):
            return True
        return False

    def is_flush(self, who_cards):
        all_cards = self.table + who_cards
        start_suit = all_cards[0][1]
        result = []
        all_cards.sort(key=lambda x: x[1])

        for i in range(1, len(all_cards)):
            if len(result) == 5:
                break
            
            if all_cards[i][1] == start_suit:
                result.append(all_cards[i])
            else:
                start_suit = all_cards[i][1]
                result.clear()
                result.append(all_cards[i])
        
        return len(result) == 5

    def is_straight(self, who_cards):
        all_cards = self.table + who_cards
        
        all_cards.sort(key=lambda x: self.custom_key(x))
        
        result = []
        start_number = self.custom_key(all_cards[0][0])

        result.append(all_cards[0])

        for i in range(1, len(all_cards)):
            if len(result) == 5:
                break
            if self.custom_key(all_cards[i][0]) == start_number + 1:
                result.append(all_cards[i])
                start_number = self.custom_key(all_cards[i][0]) 
            else:
                result.clear()
                result.append(all_cards[i])
                start_number = self.custom_key(all_cards[i][0])
        
        return len(result) == 5
    
    def is_three_of_a_kind(self, who_cards):
        all_cards = self.table + who_cards
        start_number = all_cards[0][0]
        result = []
        all_cards.sort(key=lambda x: x[0])

        for i in range(1, len(all_cards)):
            if len(result) == 3:
                break

            if all_cards[i][0] == start_number:
                result.append(all_cards[i])
            else:
                start_number = all_cards[i][0]
                result.clear()
                result.append(all_cards[i])
        
        return len(result) == 3

    def is_pair(self, who_cards, table=None):
        if table is None:
            all_cards = self.table + who_cards
        else:
            all_cards = self.table + who_cards
            all_cards.remove(table[0])
            all_cards.remove(table[1])

        all_cards.sort(key=lambda x: x[0])


        start_number = all_cards[0][0]
        result = []
        result.append(all_cards[0])

        for i in range(1, len(all_cards)):
            if all_cards[i][0] == start_number:
                result.append(all_cards[i])
                break
            else:
                start_number = all_cards[i][0]
                result.clear()
                result.append(all_cards[i])
        
        return len(result) == 2, result

    def is_two_pair(self, who_cards):
        test1, result1 = self.is_pair(who_cards)
        if test1:
            test2 = self.is_pair(who_cards, result1)[0]
        return test1 and test2

    def custom_key(self, x):
        value_map = {"A": 14, "J": 11, "K": 13, "Q": 12}

        return value_map[x[0]] if x[0] in value_map else int(x[0])
    
    # decision making    
    def evaluation(self):
        hand = self.Hand_ranking(self.computer.hand)
        if hand > 5:
            return "strong"
        elif hand > 3:
            return "medium"
        else:
            return "weak"
           
    def strong(self, previous):
        if rd() > 0.5:
            return list(self.strong_bluff(previous))
        return list(self.strong_no_bluff(previous))
    
    def medium(self, previous):
        if rd() > 0.7:
            return list(self.medium_bluff(previous))
        return list(self.medium_no_bluff(previous))

    def weak(self, previous):
        if rd() > 0.85:
            return list(self.weak_bluff(previous))
        return list(self.weak_no_bluff(previous))
    
    def strong_bluff(self, previous):
        if previous == "all_in":
            return "call", -1
        else:
            if len(self.table) == 5 and rd() > 0.5:
                return "all in", -1
            if previous == "raise":
                return "call" , -1
            return "raise", randint(int(self.computer.balance/10), int(self.computer.balance/3))

    def strong_no_bluff(self, previous):
        if previous == "all_in":
            return "call", -1
        else:
            if rd() >= 0.5 and previous != "raise":
                return "raise", randint(int(self.computer.balance/10), int(self.computer.balance/3))
            return "all in", -1

    def medium_bluff(self, previous):
        if previous == "all_in" and rd() > 0.5:
            return "call", -1
        if previous == "raise" and rd() < 0.8:
            return "call", -1
        return "raise", randint(0, int(self.computer.balance/4))
        

    def medium_no_bluff(self):
        return "call", -1

    def weak_bluff(self, previous):
        if previous == "all_in" and rd() < 0.1:
            return "call", -1
        if previous == "raise":
            if rd() < 0.4:
                return "call"
            return "fold", -1
        if rd() < 0.2:
            return "raise", randint(0, int(self.computer.balance/4))
        return "fold", -1
    
    def weak_no_bluff(self, previous):
        if previous == "call" and rd() > 0.3:
            return "call", -1
        return "fold", -1