import random

def displayTitle():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def cardDeck():
    cardSuits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    cardRanks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    cardValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = []
    while True:
        for suit in cardSuits:
            for rank in cardRanks:
                deck.append(rank + " of " + suit)
        return deck
        break

    




def main():
    displayTitle()
    cardDeck()

    




if __name__ == "__main__":
    main()
