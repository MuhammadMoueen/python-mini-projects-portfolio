# Import required libraries
import json

# Define the JSON file name for storing inventory data
FILE_NAME = "inventory.json"


class Item:
    """Represents an inventory item with name, quantity, and price."""
    
    def __init__(self, name, quantity, price):
        """Initialize an item with name, quantity, and price."""
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convert item object to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


def load_items():
    """Load inventory items from JSON file.
    
    Returns:
        list: List of items from file, or empty list if file doesn't exist.
    """
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        # Return empty list if file doesn't exist or is corrupted
        return []


def save_items(items):
    """Save inventory items to JSON file.
    
    Args:
        items (list): List of item dictionaries to save.
    """
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


def show_items(items):
    """Display all items in the inventory.
    
    Args:
        items (list): List of item dictionaries to display.
    """
    if not items:
        print("\nInventory empty.")
        return

    print("\n--- INVENTORY ---")
    # Loop through each item and display its details
    for item in items:
        print(f"{item['name']} | Qty: {item['quantity']} | Price: {item['price']}")


def add_item(items):
    """Add a new item to the inventory.
    
    Args:
        items (list): List of existing items to add to.
    """
    # Get item details from user
    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    # Create new item object and add to inventory
    item = Item(name, quantity, price)
    items.append(item.to_dict())
    save_items(items)
    print("Item added!")


def update_stock(items):
    """Update the quantity of an existing item.
    
    Args:
        items (list): List of items to search and update.
    """
    name = input("Enter item name: ")

    # Search for item by name (case-insensitive)
    for item in items:
        if item["name"].lower() == name.lower():
            item["quantity"] = int(input("New quantity: "))
            save_items(items)
            print("Stock updated!")
            return

    # If item not found after searching all items
    print("Item not found!")


def generate_report(items):
    """Generate a financial report of the inventory.
    
    Args:
        items (list): List of items to generate report for.
    """
    print("\n--- INVENTORY REPORT ---")

    total_value = 0

    # Calculate value for each item (quantity × price)
    for item in items:
        value = item["quantity"] * item["price"]
        total_value += value
        print(f"{item['name']} → Stock Value: {value}")

    # Display total value of all inventory
    print("Total Inventory Value:", total_value)


def main():
    """Main function to run the inventory management system."""
    # Load existing inventory from file
    items = load_items()

    # Main menu loop
    while True:
        print("\n--- INVENTORY SYSTEM ---")
        print("1. View Items")
        print("2. Add Item")
        print("3. Update Stock")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose option: ")

        # Execute action based on user choice
        if choice == "1":
            show_items(items)
        elif choice == "2":
            add_item(items)
        elif choice == "3":
            update_stock(items)
        elif choice == "4":
            generate_report(items)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


# Run the program
if __name__ == "__main__":
    main()
