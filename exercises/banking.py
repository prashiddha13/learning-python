
'''
This does not store the data from the previous run, so the balance always starts at zero. But we can use this in simpler way just adding and withdrawing the amount while running. 
'''
def show_balance(balance):
    print(f"Your balance is Rs. {balance:,.2f}")

def deposit():
    amount = float(input("What amount would you like to deposit?: ").strip())

    if amount < 0:
        print("Negative amounts are invalid. ")
        return 0
    elif amount == 0:
        return amount
    elif amount > 0:
        return amount
    else:
        print("Invalid input. ")
        return 0

def withdraw(balance):
    amount = float(input("What amount would you like to withdraw?: ").strip())

    if amount < 0:
        print("Negative amounts are invalid. ")
        return 0
    elif amount == 0:
        return amount
    elif amount > 0:
        if amount > balance:
            print("Insufficient balance to withdraw that amount. ")
            amount = 0 
        else:
            pass

        return amount
    else:
        print("Invalid input. ")
        return 0
def main():
    
    balance = 0
    running = True

    while running: 
        print()
        print("****************************")
        print("    Welcome to the Bank!    ")
        print("****************************")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit. ")
        print("****************************")

        choice = int(input("Enter your choice. (1-4): ").strip())
    
        print("____________________________")
        print()

        if choice == 1:
            show_balance(balance) #Done. 
        elif choice == 2:
            balance += deposit() #amount from the deposit function we defined will take the value here in place of deposit because we called it. 
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            running = False 
        else:
            print("This is not a valid option. ")
        
    print("Thanks for using our service. ")

if __name__ == "__main__":
    main()
