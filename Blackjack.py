import random
from db import *


def displayTitle():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def cardDeck(cardSuits, cardRanks, deck):
    for suit in cardSuits:
        counter = 0
        for rank in cardRanks:
            card=[]
            card.append(rank)
            card.append("of")
            card.append(suit)
            deck.append(card)
            counter += 1
    return deck

def betting(chips):
    print()
    print("Feeling lucky?")
    while True:
        try:
            betAmount = int(input("How much would you like to bet? "))
            print()
        except ValueError as e:
            print("I'm sorry. You have entered an invalid amount.")
            print("Please try again.")
            continue
        if betAmount < 0:
            print("I'm sorry. You have entered an invalid amount.")
            print("Please try again.")
            continue
        confirmBetAmount = input("Are you sure you want to bet " + str(betAmount) + "? (y/n): ")
        if confirmBetAmount.lower() == "y":
            print("You have wagered " + str(betAmount) + " chips. Good luck!")
            playerMoney = []
            remainingChips = chips - betAmount
            playerMoney.append(remainingChips)
            print()
            while True:
                try:
                    with open(FILENAME, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(playerMoney)
                        break
                except Exception as e:
                    print(type(e), e)
                    print("Uh-oh! Looks like something went wrong.")
                    print("Unable to wager chips. Sorry!")
                    print("I am going to have to ask you to leave the casino. Goodbye.")
                    sys.exit()
        else:
            print("Changed your mind?")
            continue       
        break
            

    '''if chips < 5:
        print("Uh-oh! It looks like you are out of chips!")
        print()
        purchaseAdditionalChips = input("Would you like to purchase additional chips?? (y/n): ")
        if purchaseAdditionalChips.lower() == "y":
            while True:
                try:
                    additionalChips = int(input("How many would you like to purchase?: "))
                    print()
                    break
                except ValueError as e:
                    print("I'm sorry. You have entered an invalid amount.")
                    print("Please try again.")
                    continue

                if additionalChips < 0:
                    print("I'm sorry. You have entered an invalid amount.")
                    print("Please try again.")
                    continue'''


def playerHand(deck):
    playerHand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card[0] == 11:
            card[0] = "J"
        if card[0] == 12:
            card[0] = "Q"
        if card[0] == 13:
            card[0] = "K"
        if card[0] == 14:
            card[0] = "A"
        playerHand.append(card)
    return playerHand
                

def dealerHand(deck):
    dealerHand = []
    for i in range(2):
        card = deck.pop()
        if card[0] == 11:
            card[0] = "J"
        if card[0] == 12:
            card[0] = "Q"
        if card[0] == 13:
            card[0] = "K"
        if card[0] == 14:
            card[0] = "A"
        dealerHand.append(card)
    return dealerHand        

def main():
    cardSuits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    cardRanks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    deck = []

    readMoney()
    displayTitle()

    chips = gettingChips()
    betting(chips)
    
    
    
    cardDeck(cardSuits, cardRanks, deck)
    print(deck)
    print()


    playerHand(deck)
    pHand = playerHand(deck)
    print(pHand)

    dealerHand(deck)
    dHand = dealerHand(deck)
    print(dHand)
    print(len(deck))




if __name__ == "__main__":
    main()
