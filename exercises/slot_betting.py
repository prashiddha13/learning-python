'''
'return' sends a value from the function back to where the function was called.
fn_name(something) calls the function fn_name() and passes 'something' as an argument.
'''
import random

def spin_row():
    symbols = ["🍌 ", "💵 ", "🪙 ", "💎 ", "🤑 ", "💣 "]

    return [random.choice(symbols) for every_iteration in range(3)]

'''
    This is the alternative (lengthier) way: 
    results = []
    for every_iteration in range(3):
        results.append(random.choice(symbols))
    return results
'''
def print_row(row):
    '''
    for randomspin in row:
        print(randomspin, end = " | ")
    print()
    this gives output as "🤑  | 🤑  | 💵  | " and final separator makes it look bad. Thus,
    '''
    print(" | ".join(row))

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "💵 ":
            return bet * 10
        elif row[0] == "🪙 ":
            return bet * 25
        elif row[0] == "💎 ":
            return bet * 50
        elif row[0] == "🤑 ":
            return bet * 100
        elif row[0] == "🍌 ":
            return bet * -25
        elif row[0] == "💣 ":
            return bet * -100
    else:
        return 0
def main():
    #This is such that user buys a ticket at the counter of the casino first for $1000 and then comes to play, so the initial balance is already $1000. 
    balance = 1000
    #I could have just printed these but this way it is fun (though it might be slower)
    symbols = ["🍌 ", "💵 ", "🪙 ", "💎 ", "🤑 ", "💣 "]
    print("--------------------------------------")
    print("Symbols: ", end = "")
    for symbol in symbols:
        print(symbol, end = " ")
    print()
    print("--------------------------------------")
    print(f"Current balance: ${balance}")

    while balance > 0:

        bet = input("Place your bet: ").strip() 
        try:
            bet = int(bet)
        except ValueError:
            print("Invalid input. Please place your bet using digits.")
            continue

        if bet <= 0:
            print("Bet must be greater than 0. ")
            continue
        elif bet > balance:
            print("Insufficient balance to place that bet. ")
            continue
        else:
            balance -= bet

        print("--------------------------------------")
        print("Spin results: ", end = " ")
        row = spin_row() #The list [random.choice(symbols) for every_iteration in range(3)] is returned through spin_row()
        print_row(row)
        print("--------------------------------------")

        prize = payout(row, bet)

        if prize > 0:
            print(f"Congratulations, You Won ${prize}")
        elif prize == 0:
            print("Better luck next time. ")
        else:
            print(f"Oh no! You Lost ${-prize}")

        balance += prize

        print(f"Current balance: ${balance}")
        print()

        if balance > 0:
            if not input("Do you want to continue? (Y/N): ").strip().upper() == "Y":
                break
            else:
                continue
        elif balance < 0:
            break


    print("Game is over!")
    print()
    if balance > 0:
        print(f"Your wallet has ${balance}")
    elif balance == 0:
        print("Your wallet is empty")
    else:
        print(f"You have ${balance} amount due. Pay at the counter. ")


if __name__ == "__main__":
    main()