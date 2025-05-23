import random
import time
print("Hello, welcome to Blackjack")
menu_option = int(input("Press 1 to play, press 2 to explain the rules ")) 
if menu_option == 1:
    card_four = random.randint(1, 13)
    card_three = random.randint(1, 13)
    card_two = random.randint(1, 13)
    card_one = random.randint(1, 13)
    dealer_one = random.randint(1, 13)
    dealer_two = random.randint(1, 13)
    dealer_three = random.randint(1, 13)
    if card_four == 11:
        card_four = 10
    elif card_four == 12:
        card_four = 10
    elif card_four == 13:
        card_four = 10
    if card_three == 11:
        card_three = 10
    elif card_three == 12:
        card_three = 10
    elif card_three == 13:
        card_three = 10
    if dealer_one == 11:
        dealer_one = 10
    elif dealer_one == 12:
        dealer_one = 10
    elif dealer_one == 13:
        dealer_one = 10
    if dealer_two == 11:
        dealer_two = 10
    elif dealer_two == 12:
        dealer_two = 10
    elif dealer_two == 13:
        dealer_two = 10
    if dealer_three == 11:
        dealer_three = 10
    elif dealer_three == 12:
        dealer_three = 10
    elif dealer_three == 13:
        dealer_three = 10
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
    if card_one == 1 and card_two == 10:
        print("You have a BLACKJACK, you win!")
    elif card_one == 10 and card_two == 1:
        print("You have a BLACKJACK, you win!")
    else:
        print(("Ok, your cards are a "),  card_one,  ("and a"),  card_two,)
        print(("My cards are a "), dealer_one, (" and a ???"))
        
        choice_one = int(input("Press 1 to hit, 2 to stay "))
        if choice_one == 1:
            print(("You chose to hit and got a"), card_three, )
            print(("You now have a total of "), card_one + card_two + card_three)
            if card_one + card_two + card_three > 21:
                print("You have lost!")
            else:
                
                choice_two = int(input("Now, press 1 to hit again or press 2 to stay"))
            
        elif choice_one == 2:
            print("You have decided to stay")
            print(("My other card is a "), dealer_two )
            if dealer_one + dealer_two >= card_one + card_two:
                print("I have won! You have lost!")
            else:
                print(("I have "), dealer_one + dealer_two)
                time.sleep(2)
                if dealer_one + dealer_two <= 16:
                    print(("I shall hit, gaining me a "), dealer_three)
                    time.sleep(1)
                    
