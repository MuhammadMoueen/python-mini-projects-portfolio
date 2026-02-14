# Bank Management System

A simple yet functional bank management system built with Python using Object-Oriented Programming (OOP) principles. This console-based application allows users to manage bank accounts with basic operations like deposits, withdrawals, and balance inquiries.

## Features

- **Create Account**: Create new bank accounts with a unique name
- **Deposit Money**: Add funds to existing accounts
- **Withdraw Money**: Withdraw funds with balance validation
- **Check Balance**: View current account balance
- **Data Persistence**: All account data is saved to a text file and persists between sessions
- **Input Validation**: Handles invalid inputs gracefully

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/bank-management-system.git
cd bank-management-system
```

2. Run the program:
```bash
python bank.py
```

## Usage

When you run the program, you'll see a menu with the following options:

```
--- BANK SYSTEM ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
```

### Creating an Account
1. Select option `1`
2. Enter the account holder's name
3. Account is created with an initial balance of 0

### Making a Deposit
1. Select option `2`
2. Enter the account name
3. Enter the deposit amount
4. Funds will be added to the account

### Making a Withdrawal
1. Select option `3`
2. Enter the account name
3. Enter the withdrawal amount
4. Funds will be deducted if sufficient balance exists

### Checking Balance
1. Select option `4`
2. Enter the account name
3. Current balance will be displayed

## File Structure

```
bank-management-system/
│
├── bank.py           # Main application file
├── accounts.txt      # Auto-generated file storing account data
└── README.md         # Project documentation
```

## Technical Details

### Class Structure

- **BankAccount**: Main class representing a bank account
  - `__init__(name, balance)`: Constructor to initialize account
  - `deposit(amount)`: Method to add funds
  - `withdraw(amount)`: Method to deduct funds
  - `show_balance()`: Method to display current balance

### Data Storage

Account data is stored in `accounts.txt` in the following format:
```
AccountName,Balance
```

## Example Usage

```
--- BANK SYSTEM ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
Choose option: 1
Enter account name: John Doe
Account created!

--- BANK SYSTEM ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
Choose option: 2
Enter account name: John Doe
Enter deposit amount: 1000
Deposit successful!

--- BANK SYSTEM ---
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
Choose option: 4
Enter account name: John Doe
Current Balance: 1000.0
```

## Future Enhancements

- Add account number generation
- Implement password/PIN protection
- Add transaction history
- Support for multiple account types (Savings, Checking, etc.)
- Database integration (SQLite/MySQL)
- GUI interface
- Interest calculation
- Transfer money between accounts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## Contact

For any questions or suggestions, please open an issue or contact me at your.email@example.com
