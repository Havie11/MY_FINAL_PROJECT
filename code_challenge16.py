#   Breaks down the Filipino denomination into bills and coins.
def breakdown_denomination(amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    denominations_names = ["P1000 bill", "P500 bill", "P200 bill", "P100 bill",
                            "P50 bill", "P20 bill", "P10 coin", "P5 coin", "P1 coin"]
    breakdown = {}
    for i, denomination in enumerate(denominations):
        count = amount // denomination
        if count > 0:
            breakdown[denominations_names[i]] = count
        amount -= count * denomination
    return breakdown

#   Creates a new banking account.
def create_account():
    name = input("Enter your name: ")
    while True:
        try:
            initial_deposit = float(input("Enter initial deposit: "))
            if initial_deposit > 0:
                break
            else:
                print("Initial deposit must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    account = {"name": name, "balance": initial_deposit}
    print(f"Account created for {name} with an initial balance of {initial_deposit:}")
    print_denomination(account["balance"])
    return account

#   Deposits the money into the account.
def deposit(account):
    while True:
        try:
            deposit_amount = float(input("Enter deposit amount: "))
            if deposit_amount > 0:
                break
            else:
                print("Deposit amount must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    account["balance"] += deposit_amount
    print(f"Deposited {deposit_amount:}. New balance: {account['balance']:}")
    print_denomination(account["balance"])

#   Withdraws the money from the account.
def withdraw(account):
    while True:
        try:
            withdraw_amount = float(input("Enter withdraw amount: "))
            if 0 < withdraw_amount <= account["balance"]:
                break
            else:
                print("Insufficient funds or invalid withdraw amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    account["balance"] -= withdraw_amount
    print(f"Withdrew {withdraw_amount:}. New balance: {account['balance']:}")
    print_denomination(account["balance"])

#   Prints the denomination breakdown of the balance.
def print_denomination(balance):
    breakdown = breakdown_denomination(balance)
    print("Denomination breakdown:")
    for denomination, count in breakdown.items():
        print(f"{denomination}: {count}")

if __name__ == "__main__":
    account = None
    while True:
        if account is None:
            account = create_account()
        else:
            print("\nChoose an action:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Enter your choice: ")
            
            if choice == "1":
                deposit(account)
            elif choice == "2":
                withdraw(account)
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")