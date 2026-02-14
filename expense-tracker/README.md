# Expense Tracker

A simple command-line expense tracking application built with Python. Track your daily expenses, categorize them, and view monthly summaries - all stored in a CSV file.

## Features

- ✨ **Add Expenses**: Record expenses with amount, category, date, and optional notes
- 📊 **View All Expenses**: Display all recorded expenses in a formatted table with totals
- 📅 **Monthly Totals**: See expense summaries grouped by month
- 💾 **Persistent Storage**: All data is saved in a CSV file (`expenses.csv`)
- ✅ **Input Validation**: Ensures valid amounts and date formats
- 🎯 **Simple Interface**: Easy-to-use menu-driven command-line interface

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MuhammadMoueen/python-expense-tracker.git
cd python-expense-tracker
```

2. Run the program:
```bash
python expense_tracker.py
```

## Usage

### Starting the Application

Run the script to launch the expense tracker:
```bash
python expense_tracker.py
```

### Menu Options

The application presents a menu with the following options:

1. **Add Expense** - Record a new expense
2. **View All Expenses** - Display all recorded expenses
3. **View Monthly Totals** - Show expense summaries by month
4. **Exit** - Close the application

### Adding an Expense

When adding an expense, you'll be prompted for:
- **Amount**: The expense amount (must be a positive number)
- **Category**: Type of expense (e.g., Food, Transport, Bills, etc.)
- **Date**: Date of expense in YYYY-MM-DD format (press Enter for today's date)
- **Note**: Optional description or note about the expense

Example:
```
Enter amount: $25.50
Category (Food/Transport/Bills/etc): Food
Date (YYYY-MM-DD) or press Enter for today: 
Note (optional): Lunch with colleagues

✓ Added: $25.5 for Food
```

### Viewing Expenses

**View All Expenses** displays a formatted table:
```
Date         Amount     Category        Note                          
-------------------------------------------------------------------
2026-02-10   $25.50     Food            Lunch with colleagues         
2026-02-09   $50.00     Transport       Gas                           
-------------------------------------------------------------------
Total:       $75.50
```

**View Monthly Totals** shows spending by month:
```
Month        Total     
----------------------
2026-02      $75.50
2026-01      $320.00
```

## File Structure

```
expense-tracker/
│
├── expense_tracker.py    # Main application file
├── expenses.csv          # Data storage (created automatically)
└── README.md            # This file
```

## Data Storage

Expenses are stored in `expenses.csv` with the following structure:
```csv
date,amount,category,note
2026-02-10,25.50,Food,Lunch with colleagues
2026-02-09,50.00,Transport,Gas
```

## Code Features

- **CSV File Handling**: Reads and writes data using Python's `csv` module
- **Data Validation**: Input validation for amounts and dates
- **Error Handling**: Try-except blocks to handle file and input errors
- **Dictionary Storage**: Each expense is stored as a dictionary for easy access
- **Date Management**: Uses `datetime` module for date handling and formatting

## Example Session

```
==================================================
  Welcome to Expense Tracker!
==================================================
✓ Loaded 2 expenses from file.

========================================
     EXPENSE TRACKER
========================================
1. Add Expense
2. View All Expenses
3. View Monthly Totals
4. Exit
========================================

Enter choice (1-4): 1

--- Add New Expense ---
Enter amount: $15.75
Category (Food/Transport/Bills/etc): Food
Date (YYYY-MM-DD) or press Enter for today: 
Note (optional): Coffee and snack

✓ Added: $15.75 for Food
✓ Saved successfully!
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available for personal and educational use.

## Author

Muhammad Moueen

## Future Enhancements

Potential features to add:
- [ ] Edit or delete existing expenses
- [ ] Filter expenses by category or date range
- [ ] Export reports to PDF or Excel
- [ ] Add budget tracking and alerts
- [ ] Visualize spending with charts
- [ ] Support for multiple currencies
- [ ] Search functionality

---

**Happy Expense Tracking! 💰**
