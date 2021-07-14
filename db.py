import csv
import sys

FILENAME = "playerMoney.csv"

def readMoney(playerMoney):
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
        
def writeMoney(playerMoney):
    while True:
        try:
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(playerMoney)
                return playerMoney
        except Exception as e:
            print(type(e), e)
            print("Uh-oh! Looks like something went wrong.")
            print("Unable to provide chips. Sorry!")
            print("Unfortunately, we have to terminate the program. Goodbye.")
            sys.exit()

def main():

    readMoney(playerMoney, chips)   
    writeMoney(playerMoney, chips)
    
if __name__ == "__main__":
    main()
