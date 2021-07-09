import csv
import sys

FILENAME = "playerMoney.csv"

def readMoney():
    playerMoney = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                playerMoney.append(row)
        return playerMoney
    except FileNotFoundError as e:
        print("Unable to find file: " + FILENAME + ".")
        print("As a result the program is terminated.")
        print("Please locate file and try again.")
        print("Goodbye.")
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()

def gettingChips():
    purchaseChips = input("Would you like to purchase some chips? (y/n): ")
    print()
    if purchaseChips.lower() == "y":
        while True:
            try:            
                chips = int(input("How many would you like to purchase?: "))
                print()
                break
            except ValueError as e:
                print("I'm sorry. You have entered an invalid amount.")
                print("Please try again.")
                continue
            
            if chips < 0:
                print("I'm sorry. You have entered an invalid amount.")
                print("Please try again.")
                continue
        
        confirmPurchase = input("Are you sure you want to purchase " + str(chips) + " chips? (y/n): ")
        if confirmPurchase.lower() == "y":
            print(str(chips) + " chips have been added to your account.")
            print("Enjoy!")
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
        else:
            print("Changed your mind? Maybe next time.")
            print("Goodbye.")
            sys.exit()
    else:
        print("Maybe another time then?")
        print("Goodbye.")
        sys.exit()
    return chips

def main():
    readMoney()

    gettingChips()


if __name__ == "__main__":
    main()
