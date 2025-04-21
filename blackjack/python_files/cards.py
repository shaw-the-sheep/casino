from random import sample as sam
from PIL import ImageTk, Image


class Cards:
    def __init__(self):
        self._deck = []

    @property
    def deck(self):
        return self._deck 
    def creat_cards(self):
        self._deck = []
        # Step 1: Define ranks and suits
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        # Step 2: Create the deck by combining each rank with each suit
        self._deck = [(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        print("Shuffling deck...")

    def dealing(self, player, nbr = 1):
        # Step 3: Function to deal two random cards without altering the deck
        hand = sam(self.deck, nbr)
        result = []

        for card in hand:
            self.deck.remove(card)
            player.hand.append(card)
            result.append(f"{card[0]}_of_{card[1]}")

        return result
    
    def resize(self, card):
        image = Image.open(f"cards_img/{card}.png")
        new_image = image.resize((150, 218))
        return ImageTk.PhotoImage(new_image)


    def total(self, hand):
        total = 0
        for card in hand:
            if card[0] in ['J', 'Q', 'K']:
                total += 10
            elif card[0] == 'A' and total + 11 <= 21:
                total += 11
            elif card[0] == 'A':
                total += 1
            else:
                total += int(card[0])

        return total