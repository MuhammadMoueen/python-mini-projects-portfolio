# Simple Bank Management System using OOP

FILE_NAME = "accounts.txt"


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return
        self.balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print("Withdrawal successful!")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")


def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        for acc in accounts:
            file.write(f"{acc.name},{acc.balance}\n")


def load_accounts():
    accounts = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, balance = line.strip().split(",")
                accounts.append(BankAccount(name, float(balance)))
    except FileNotFoundError:
        pass
    return accounts


def find_account(accounts, name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None


def main():
    accounts = load_accounts()

    while True:
        print("\n--- BANK SYSTEM ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter account name: ")
            accounts.append(BankAccount(name))
            save_accounts(accounts)
            print("Account created!")

        elif choice == "2":
            name = input("Enter account name: ")
            acc = find_account(accounts, name)

            if acc:
                try:
                    amount = float(input("Enter deposit amount: "))
                    acc.deposit(amount)
                    save_accounts(accounts)
                except:
                    print("Enter valid number!")
            else:
                print("Account not found!")

        elif choice == "3":
            name = input("Enter account name: ")
            acc = find_account(accounts, name)

            if acc:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    acc.withdraw(amount)
                    save_accounts(accounts)
                except:
                    print("Enter valid number!")
            else:
                print("Account not found!")

        elif choice == "4":
            name = input("Enter account name: ")
            acc = find_account(accounts, name)

            if acc:
                acc.show_balance()
            else:
                print("Account not found!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


main()
