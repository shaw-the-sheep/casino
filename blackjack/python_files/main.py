from player import Player
from cards import Cards
from interface import Interface
from time import sleep

# Creating players
while True:
    try:
        p1 = Player(input("Name: "), float(input("Balance: ")))
        p2 = Player("dealer") 
        break
    except ValueError:
        print("Invalid input. Please try again.")
    except AssertionError as e:
        print("Invalid input. Please try again.")

init_balance = p1.balance
print(init_balance)

while True:
    card = Cards()
    # placing the bet
    while True:
        try:
            bet = int(input("Bet: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            break
    p1.add_bet(bet)

    # Schuffling the deck
    card.shuffle()
    sleep(2)

    # Dealing cards
    p1.hand = card.dealing(p1.name)
    p2.hand = card.dealing(p2.name)

    # getting totals
    p1.points = card.total(p1.hand)
    p2.points = card.total(p2.hand)

    sleep(1)
    print(f"Hand of {p1.name}: {p1.hand[0][0]} {p1.hand[0][1]:10} and {p1.hand[1][0]} {p1.hand[1][1]:10}. Your total is {p1.points}")
    sleep(3)
    print(f"Hand of {p2.name}: {p2.hand[0][0]} {p2.hand[0][1]:10} and {p2.hand[1][0]} {p2.hand[1][1]:10}. Your total is {p2.points}")
    sleep(2)

    # Player's turn
    while p1.points < 21 and p2.points < 21:
        choice = input("Would you like to hit or stand? (h/s): ")
        if choice.lower() == "h":
            p1.play()

            sleep(2)

            p2.play()

        elif choice.lower() == "s":
            if p2.points < 14:
                p2.play()
            else:
                print("Dealer stands.")
            break
        else:
            print("Invalid input. Please try again.")

    sleep(3)
    
    # choose a winner
    if p1.points == 21 and p2.points != 21:
        print("Blackjack!")
        ratio = 3
        p1.winning_bet(bet, ratio)
    elif p2.points == 21 and p1.points != 21:
        print(f"{p2.name} has a Blackjack!")
        ratio = 0.5
        p1.add_bet(bet * ratio)
    elif p1.points > 21 and p2.points < 21:
        print(f"{p1.name} busted. {p2.name} wins!")
    elif p2.points > 21 and p1.points < 21:
        print(f"{p2.name} busted. {p1.name} wins!")
        ratio = 1.5
        p1.winning_bet(bet, ratio)
    elif p1.points > p2.points:
        print(f"{p1.name} wins!")
        ratio = 2
        p1.winning_bet(bet, ratio)
    elif p2.points > p1.points:
        print(f"{p2.name} wins!")
    else:
        print("It's a tie!")
        ratio = 1
        p1.winning_bet(bet, ratio)

    if p1.balance <= 0:
        print("You ran out of money. Game over.")
        break
    
    new_game = input("Would you like to play again? (y/n): ")
    if new_game.lower() == "y":
        print("--------------------------------")
        continue
    elif new_game.lower() == "n": 
        difference = init_balance - p1.balance
        if difference > 0:
            print(f"You won {difference}!")
        else:
            print(f"You lost {-difference}!")  
        break
    else:
        print("Invalid input. Please try again.")