import random


while True:
    print("Welcome to blackjack!")
    # Creates the variable hand which gets assigned a random integer between 1 and 11 
    # and is printed to the console so the player knows what card they have been dealt
    face_cards = ["Q", "K", "J"]
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ace = ["A"]
    the_cards = cards + face_cards + ace
    hand = random.choice(the_cards)
    print("Your hand is:", hand)
    if hand in ace:
        hand = 11
    if hand in face_cards:
            hand = 10
    # Blackjack loop which goes on until the player chooses to stand or busts by going over 21
    while hand < 21:
        hit = input("Do you want to hit? (yes/no): ")
        if hit == "yes":
            new_card = random.choice(the_cards)
            print("You drew:", new_card)

            if new_card in face_cards:
             new_card = 10

            if new_card in ace:
                if hand + 11 > 21:
                    new_card = 1
                else: new_card = 11
            hand += new_card
            print("Your new hand is:", hand)
        elif hit == "no":
            print("You chose to stand.")
            break

    if hand == 21:
        print("You win!") # The player wins if they get a blackjack (21) and the game ends.

    elif hand > 21:
        print("You busted!") # The player loses if they bust and go over 21 and the game ends.

    else:
        dealer_hand = random.choice(the_cards)   
            # The dealer's hand is created and assigned a random integer between 1 and 11.
        print("Dealer's hand is:", dealer_hand)
        if dealer_hand in ace:
            dealer_hand = 11
        if dealer_hand in face_cards:
            dealer_hand = 10
        while dealer_hand < 17:                     # A loop is created so the dealer will keep drawing cards until they reach 17 or higher.
            new_card = random.choice(the_cards)
                # The dealers new and old cards are added togeher so the player knows the dealers new hand.
            print("Dealer drew:", new_card)
            if new_card in face_cards:
             new_card = 10
            if new_card in ace:
                if dealer_hand + 11 > 17:
                 new_card = 1
                else: new_card = 11
            
            dealer_hand = dealer_hand + new_card
            print("Dealer's new hand is:", dealer_hand)
    
        if dealer_hand > 21:                               # If the dealer busts by going over 21 the player wins and the game ends.
            print("Dealer busts! You win!")
        elif hand > dealer_hand:                  # If the players hand is greater than the dealers hand the player wins and the game ends.
            print("You win!")
        elif hand < dealer_hand:                 #If the dealer has a greater hand than the player the dealer wins and the game ends.
            print("Dealer wins!")
        else:                                  # If the player has the same hand as the dealer the game ends in a tie.
            print("It's a tie!")
    
    choice = input("Do you want to play again? (yes/no): ")
    if choice != "yes":
        print("Goodbye...")
        break
