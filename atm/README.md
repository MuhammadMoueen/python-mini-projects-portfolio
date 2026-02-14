# ATM Machine System

A simple command-line ATM (Automated Teller Machine) simulator built with Python.

## Features

- **PIN Authentication**: Secure login with PIN verification
- **Check Balance**: View current account balance
- **Deposit Money**: Add funds to your account
- **Withdraw Money**: Withdraw funds from your account
- **Input Validation**: Handles invalid amounts and insufficient balance

## How to Use

1. **Run the program**:
   ```bash
   python atm.py
   ```

2. **Enter PIN**: The default PIN is `1234`

3. **Choose from the menu options**:
   - `1` - Check Balance
   - `2` - Deposit
   - `3` - Withdraw
   - `4` - Exit

## Default Account Details

- **Name**: User
- **PIN**: 1234
- **Initial Balance**: 1000

## Requirements

- Python 3.x

## Code Structure

The project consists of:
- `BankAccount` class: Manages account operations (balance, deposit, withdraw)
- `main()` function: Handles user interface and menu navigation

## Example Usage

```
=== ATM MACHINE ===
Enter PIN: 1234
Login successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Choose option: 1
Your balance is: 1000
```

## Future Enhancements

- Multiple user accounts
- Transaction history
- Password encryption
- Database integration
- GUI interface

## License

This project is open source and available for educational purposes.
