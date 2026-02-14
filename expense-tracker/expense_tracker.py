# Step 1: Import required libraries
import csv           # For reading and writing CSV files
import os            # For checking if file exists
from datetime import datetime  # For working with dates
# Step 2: Global variables
EXPENSES_FILE = "expenses.csv"  # Name of file to store expenses
expenses = []  # Empty list to store all expense records in memory

# ============================================
# FUNCTION 1: Load expenses from CSV file
# ============================================
def load_expenses():

    global expenses  # Use global variable to modify the expenses list
    # Check if CSV file exists using os.path.exists()
    if os.path.exists(EXPENSES_FILE):
        try:
            # Open file in read mode
            with open(EXPENSES_FILE, 'r', newline='', encoding='utf-8') as file:
                # csv.DictReader reads CSV and converts each row to dictionary
                reader = csv.DictReader(file)
                expenses = list(reader)  # Convert to list
                print(f"✓ Loaded {len(expenses)} expenses from file.")
        except Exception as e:
            # If any error occurs, start with empty list
            print(f"Error: {e}")
            expenses = []
    else:
        # If file doesn't exist, start fresh
        print("No expense file found. Starting new.")
        expenses = []

# ============================================
# FUNCTION 2: Save expenses to CSV file
# ============================================
def save_expenses():

    try:
        # Open file in write mode (overwrites existing file)
        with open(EXPENSES_FILE, 'w', newline='', encoding='utf-8') as file:
            # Define column names for CSV
            fieldnames = ['date', 'amount', 'category', 'note']
            
            # csv.DictWriter writes dictionaries to CSV
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header row (column names)
            writer.writeheader()
            
            # Loop through each expense and write as row
            for expense in expenses:
                writer.writerow(expense)
                
        print("✓ Saved successfully!")
    except Exception as e:
        print(f"Error saving: {e}")


# ============================================
# FUNCTION 3: Add new expense
# ============================================
def add_expense():

    print("\n--- Add New Expense ---")
    
    # STEP 1: Get amount with validation
    while True:
        try:
            amount = float(input("Enter amount: $"))  # Convert string to float
            if amount <= 0:
                print("Amount must be positive!")
                continue  # Ask again
            break  # Exit loop if valid
        except ValueError:
            # If user enters non-number, show error
            print("Please enter a valid number.")
    
    # STEP 2: Get category
    category = input("Category (Food/Transport/Bills/etc): ").strip()
    if not category:  # If empty, use default
        category = "Other"
    
    # STEP 3: Get date (or use today)
    date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input:
        try:
            # Validate date format
            datetime.strptime(date_input, '%Y-%m-%d')
            date = date_input
        except ValueError:
            print("Invalid format. Using today.")
            date = datetime.now().strftime('%Y-%m-%d')  # Get today's date
    else:
        date = datetime.now().strftime('%Y-%m-%d')  # Use today
    
    # STEP 4: Get optional note
    note = input("Note (optional): ").strip()
    
    # STEP 5: Create dictionary to store expense
    # Dictionary stores data as key-value pairs
    expense = {
        'date': date,
        'amount': str(amount),  # Convert to string for CSV
        'category': category,
        'note': note
    }
    
    # STEP 6: Add to list and save to file
    expenses.append(expense)  # Add dictionary to list
    save_expenses()  # Save to CSV file
    
    print(f"\n✓ Added: ${amount} for {category}")

# ============================================
# FUNCTION 4: View all expenses
# ============================================
def view_all_expenses():

    print("\n--- All Expenses ---")
    
    # Check if list is empty
    if not expenses:
        print("No expenses yet. Add some!")
        return  # Exit function
    
    # Print table header
    print(f"{'Date':<12} {'Amount':<10} {'Category':<15} {'Note':<30}")
    print("-" * 67)  # Print separator line
    
    # Loop through each expense and calculate total
    total = 0
    for expense in expenses:  # For each dictionary in list
        # Extract values from dictionary
        date = expense['date']
        amount = float(expense['amount'])  # Convert string to float
        category = expense['category']
        note = expense['note']
        
        # Print formatted row (:<12 means left-align with 12 spaces)
        print(f"{date:<12} ${amount:<9.2f} {category:<15} {note:<30}")
        total += amount  # Add to running total
    
    # Print total at bottom
    print("-" * 67)
    print(f"{'Total:':<12} ${total:.2f}")


# ============================================
# FUNCTION 5: View monthly totals
# ============================================
def view_monthly_total():

    print("\n--- Monthly Totals ---")
    
    # Check if list is empty
    if not expenses:
        print("No expenses yet.")
        return
    
    # Create empty dictionary to store monthly totals
    # Dictionary format: {'2026-02': 150.50, '2026-03': 200.00}
    monthly_totals = {}
    
    # Loop through each expense
    for expense in expenses:
        date = expense['date']  # e.g., "2026-02-06"
        amount = float(expense['amount'])
        
        try:
            # Extract first 7 characters to get year-month
            # "2026-02-06" becomes "2026-02"
            month_key = date[:7]  # String slicing
            
            # Add amount to that month's total
            if month_key in monthly_totals:
                monthly_totals[month_key] += amount  # Add to existing
            else:
                monthly_totals[month_key] = amount  # Create new entry
        except:
            continue  # Skip if error
    
    # Display results sorted by month
    print(f"{'Month':<12} {'Total':<10}")
    print("-" * 22)
    
    # sorted() sorts dictionary keys alphabetically
    for month in sorted(monthly_totals.keys()):
        total = monthly_totals[month]
        print(f"{month:<12} ${total:.2f}")


# ============================================
# FUNCTION 6: Show menu
# ============================================
def show_menu():

    print("\n" + "=" * 40)
    print("     EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Monthly Totals")
    print("4. Exit")
    print("=" * 40)


# ============================================
# FUNCTION 7: Main function (Program starts here)
# ============================================
def main():
    
    print("\n" + "="*50)
    print("  Welcome to Expense Tracker!")
    print("="*50)
    
    # Load existing expenses from CSV file
    load_expenses()
    
    # Infinite loop - runs until user chooses to exit
    while True:
        show_menu()  # Display menu
        
        # Get user's choice
        choice = input("\nEnter choice (1-4): ").strip()
        
        # Use if-elif-else to call appropriate function
        if choice == '1':
            add_expense()  # Call function to add expense
        elif choice == '2':
            view_all_expenses()  # Call function to view all
        elif choice == '3':
            view_monthly_total()  # Call function for monthly totals
        elif choice == '4':
            print("\n✓ Thank you! Goodbye!")
            break  # Exit the while loop
        else:
            print("\n✗ Invalid! Choose 1-4.")


# ============================================
# PROGRAM ENTRY POINT
# ============================================
# This special condition checks if file is run directly
# (not imported as a module)
if __name__ == "__main__":
    main()  # Start the program
