def breakdown_denomination(amount):
    denominations = {
        1000: "P1000 bill",
        500: "P500 bill",
        200: "P200 bill",
        100: "P100 bill",
        50: "P50 bill",
        20: "P20 bill",
        10: "P10 coin",
        5: "P5 coin",
        1: "P1 coin",
    }

    breakdown = {}
    for denomination, name in denominations.items():
        count = amount // denomination
        if count > 0:
            breakdown[name] = count
            amount -= count * denomination

    return breakdown

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
    return account

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

if __name__ == "__main__":
    account = None
    while True:
        if account is None:
            account = create_account()
        else:
            print("\nChoose an action:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Break down denomination")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                deposit(account)
            elif choice == "2":
                withdraw(account)
            elif choice == "3":
                print(f"Current balance: {account['balance']:}")
            elif choice == "4":
                amount = float(input("Enter amount to break down: "))
                breakdown = breakdown_denomination(amount)
                print(f"Breakdown of {amount:}:")
                for denomination, count in breakdown.items():
                    print(f"{denomination}: {count}")
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")