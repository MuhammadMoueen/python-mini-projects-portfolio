class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print("Withdrawal successful!")


def main():
    account = BankAccount("User", "1234", 1000)

    print("=== ATM MACHINE ===")

    pin_input = input("Enter PIN: ")

    if pin_input != account.pin:
        print("Wrong PIN! Access denied.")
        return

    print("Login successful!")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid option!")


main()
