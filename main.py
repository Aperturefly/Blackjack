import random
print("Hello, welcome to Blackjack")
menu_option = int(input("Press 1 to play, press 2 to explain the rules ")) 
if menu_option == 1:
    card_two = random.randint(1, 13)
    card_one = random.randint(1, 13)
    
    if card_one == 11:
        card_one = 10
    elif card_one == 12:
        card_one = 10
    elif card_one == 13:
        card_one = 10
    if card_two == 11:
        card_two = 10
    elif card_two == 12:
        card_two = 10
    elif card_two == 13:
        card_two = 10
    print(("Ok, your cards are a "),  card_one,  ("and a"),  card_two,)
#pygame
#Define values for cards
#code rng
