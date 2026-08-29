import random

while True:
    print("Welcome to blackjack!")
# Creates the variable hand which gets assigned a random integer between 1 and 11 
# and is printed to the console so the player knows what card they have been dealt

    Q = int(10)
    J = int(10)
    K = int(10)
    hand = random.randint(1, 11) 
    print("Your hand is:", hand)
    # Blackjack loop which goes on until the player chooses to stand or busts by going over 21
    while hand < 21:
        hit = input("Do you want to hit? (yes/no): ")
        if hit == "yes":
            new_card = random.randint(1, 11) 
            hand += new_card

            print("You drew:", new_card)
            print("Your new hand is:", hand)
        elif hit == "no":
            print("You chose to stand.")
            break

    if hand == 21:
        print("You win!") # The player wins if they get a blackjack (21) and the game ends.

    elif hand > 21:
        print("You busted!") # The player loses if they bust and go over 21 and the game ends.

    else:
        dealer_hand = random.randint(1,11)         # The dealer's hand is created and assigned a random integer between 1 and 11.
        print("Dealer's hand is:", dealer_hand)

        while dealer_hand < 17:                     # A loop is created so the dealer will keep drawing cards until they reach 17 or higher.
            new_card = random.randint(1, 11)       # The dealers new card is created and assigned a random integer between 1 and 11.
            dealer_hand = dealer_hand + new_card     # The dealers new and old cards are added togeher so the player knows the dealers new hand.
            print("Dealer drew:", new_card)
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



    










##

## print("Welcome to blackjack!")

## hand = random.randint(1, 11)
## print("Your hand is: ", hand)

## stand = input("Do you want to stand? : ")

## if stand == "yes":
   ##print("You chose to stand.")

##elif stand == "no":
   ## hit = input("Do you want to hit? : ")

##
##if hit == "yes": 
   ## new_card = random.randint(1, 11)
   ## hand = hand + new_card
   ## print("You drew: ", new_card)
  ##  print("Your new hand is: ", hand)