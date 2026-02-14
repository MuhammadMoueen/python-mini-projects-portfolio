# Python Inventory Management System

A simple command-line inventory management system built with Python. This application allows you to track items, manage stock quantities, and generate inventory value reports.

## Features

- **View Inventory**: Display all items with their quantities and prices
- **Add Items**: Add new items to the inventory with name, quantity, and price
- **Update Stock**: Modify the quantity of existing items
- **Generate Reports**: Calculate and display the total value of inventory
- **Persistent Storage**: All data is saved to a JSON file for persistence

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MuhammadMoueen/python-inventory-system.git
cd python-inventory-system
```

2. No additional installation needed - just run the script!

## Usage

Run the program using Python:

```bash
python inventry.py
```

### Menu Options

Once the program starts, you'll see a menu with the following options:

1. **View Items**: Displays all items currently in the inventory
2. **Add Item**: Prompts you to enter item name, quantity, and price
3. **Update Stock**: Allows you to change the quantity of an existing item
4. **Generate Report**: Shows the stock value for each item and total inventory value
5. **Exit**: Closes the application

### Example Usage

```
--- INVENTORY SYSTEM ---
1. View Items
2. Add Item
3. Update Stock
4. Generate Report
5. Exit
Choose option: 2

Item name: Laptop
Quantity: 10
Price: 999.99
Item added!
```

## File Structure

```
inventory/
├── inventry.py      # Main application file
├── inventory.json   # Data storage file (created automatically)
└── README.md        # This file
```

## Data Storage

Inventory data is stored in `inventory.json` in the following format:

```json
[
    {
        "name": "Laptop",
        "quantity": 10,
        "price": 999.99
    },
    {
        "name": "Mouse",
        "quantity": 50,
        "price": 19.99
    }
]
```

## Code Structure

- **Item Class**: Represents individual inventory items
- **load_items()**: Loads inventory from JSON file
- **save_items()**: Saves inventory to JSON file
- **show_items()**: Displays all inventory items
- **add_item()**: Adds a new item to inventory
- **update_stock()**: Updates quantity of existing items
- **generate_report()**: Calculates and displays inventory value
- **main()**: Main program loop with menu interface

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## Future Enhancements

Potential features that could be added:
- Delete items from inventory
- Search functionality
- Price update feature
- Low stock alerts
- Export reports to CSV/PDF
- GUI interface

## License

This project is open source and available for educational purposes.

## Author

Muhammad Moueen

## Contact

For questions or suggestions, please open an issue in the GitHub repository.
