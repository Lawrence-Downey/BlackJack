import random
from db import *
import re

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
    print("Please place your bet. Minimum of 5 and Maximum of 1000.")
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
        elif betAmount > chips:
            print("I'm sorry. You do not have enough chips to place that bet.")
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
        return betAmount
            
    if chips < 5:
        print("Uh-oh! Minimum bet is 5.")
        print("Look's like you'll have to get more chips if you want to keep playing.")
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
                    continue
            confirmPurchaseAdditionalChips = input("Are you sure you want to purchase " + str(purchaseAdditionalChips) + " chips? (y/n): ")
            if confirmPurchaseAdditionalChips.lower() == "y":
                print(str(purchaseAdditionalChips) + " chips have been added to your account.")
                print("Enjoy!")
                playerMoney = []
                playerMoney.append(purchaseAdditionalchips)
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
                        print("Unable to provide chips. Sorry!")
                        print("Unfortunately, we have to terminate the program. Goodbye.")
                        sys.exit()
            else:
                print("Changed your mind? Maybe next time.")
                print("Goodbye.")
                sys.exit()
        else:
            print("Maybe another time then?")
            print("Goodbye.")
            sys.exit()
    return betAmount
def playerHand(deck):
    playerHand = []
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
        playerHand.append(card)
    return playerHand
                
def dealerHand(deck):
    dealerHand = []
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
        dealerHand.append(card)
    return dealerHand

def playerTotal(pHand):
    playerTotal = 0
    aces = 0
    for card in pHand:
        rank = card[0]
        if rank == "J" or rank == "Q" or rank == "K":
            playerTotal += 10
        elif rank == "A":
            if playerTotal >= 11:                
                playerTotal += 1
                aces += 1
            else:
                playerTotal += 11
                aces += 1
        else:
            playerTotal += int(rank)
    while aces > 0 and playerTotal < 21:
        playerTotal -= 10
        aces -= 1
    return playerTotal

def dealerTotal(dHand):
    dealerTotal = 0
    aces = 0
    for card in dHand:
        rank = card[0]
        if rank == 'J' or rank == 'Q' or rank == 'K':
            dealerTotal += 10
        elif rank == 'A':
            if dealerTotal >= 11:
                dealerTotal += 1
            else:
                dealerTotal += 11
        while aces > 0 and dealerTotal < 21:
            playerTotal -= 10
            aces -= 1
        else:
            dealerTotal += int(rank)
    return dealerTotal
            
def game(deck, pHand, dHand, playerTotal, dealerTotal):
    
    print("DEALER'S SHOW CARD:")
    print(str(dHand[0]).strip('[]').replace(",", '').replace("'", ''))
    print("???")
    print()
    print("PLAYER CARDS:")
    print(str(pHand[0]).strip('[]').replace(",", '').replace("'", ''))
    print(str(pHand[1]).strip('[]').replace(",", '').replace("'", ''))
    print()
    while True:
        choice = input("Would you like to hit or stand? ")
        if choice.lower() == "hit":
            card = deck.pop()
            if card[0] == 11:
                card[0] = "J"
            if card[0] == 12:
                card[0] = "Q"
            if card[0] == 13:
                card[0] = "K"
            if card[0] == 14:
                card[0] = "A"
            pHand.append(card)
            print("PLAYER CARDS:")
            for card in pHand:
                print(str(card).strip('[]').replace(",", '').replace("'", ''))            
            continue
        elif choice.lower() == "stand":
            print()
            break
        else:
            print("You have entered an invalid command. Please try again.")
            continue
    print("DEALER'S CARDS:")
    print(str(dHand[0]).strip('[]').replace(",", '').replace("'", ''))
    print(str(dHand[1]).strip('[]').replace(",", '').replace("'", ''))
    print()

    while dealerTotal(dHand) <= 17:
        card = deck.pop()
        if card[0] == 11:
            card[0] = "J"
        if card[0] == 12:
            card[0] = "Q"
        if card[0] == 13:
            card[0] = "K"
        if card[0] == 14:
            card[0] = "A"
        dHand.append(card)
        print("DEALER'S SHOW CARDS:")
        for card in dHand:
            print(str(card).strip('[]').replace(",", '').replace("'", ''))
        print()

    print("PLAYER POINTS: " + str(playerTotal(pHand)))
    dealerPoints = dealerTotal
    print("DEALER POINTS: " + str(dealerTotal(dHand)))
    
def score(playerTotal, dealerTotal,pHand, dHand, chips, betAmount):
    again = "y"
    while again == "y":
        if playerTotal(pHand) == 21:
            print("Congratulations! You have BlackJack!")
            winnings = betAmount * 1.5
            chips += winnings
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
        elif dealerTotal(dHand) == 21:
            chips -= betAmount
            print("Sorry, you lose. The dealer has BlackJack!")
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
        elif playerTotal(pHand) > 21:
            chips -= betAmount
            print("Sorry, you busted. Better luck next time!")
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
        elif dealerTotal(dHand) > 21:
            print("Congratulations! The dealer has busted. You win!")
            winnings = betAmount * 1.5
            chips += winnings
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
        elif playerTotal(pHand) < dealerTotal(dHand):
            chips -= betAmount
            print("Sorry, you lose. The dealer's score is higher than yours.")
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
        elif playerTotal(pHand) < dealerTotal(dHand):
            print("Congratulations! Your score is higher than the dealer's. You win!")
            winnings = betAmount * 1.5
            chips += winnings
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
        elif dealerTotal(dHand) == playerTotal(pHand):
            print("It's a draw! You and the dealer have the same score.")
            chips += betAmount
            playerMoney = []
            playerMoney.append(chips)
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
                    print("Unable to provide chips. Sorry!")
                    print("Unfortunately, we have to terminate the program. Goodbye.")
                    sys.exit()
            print("Available Chips: " + str(chips))
            print()
            break
    
def main():
    cardSuits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    cardRanks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    deck = []
    
    readMoney()
    cardDeck(cardSuits, cardRanks, deck)
    displayTitle()
    
    chips = gettingChips()
    betAmount = betting(chips)
    
    
    dealerHand(deck)
    dHand = dealerHand(deck)
    playerHand(deck)
    pHand = playerHand(deck)

    dealerTotal(dHand)
    playerTotal(pHand)
    
    again = "y"
    while again == "y":
        game(deck, pHand, dHand, playerTotal, dealerTotal)
        score(playerTotal, dealerTotal,pHand, dHand, chips, betAmount)
        again = input("Would you like to play again? (y/n): ")
        if again.lower() == "y":
            continue
        else:
            break
    print()
    print("Thanks for playing! We home to see you again soon!")
    print("Bye!")
    
        
if __name__ == "__main__":
    main()
