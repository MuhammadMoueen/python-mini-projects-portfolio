# Contact Book

A simple command-line contact management system built with Python. This application allows you to store, manage, and search contacts with ease.

## Features

- **View Contacts**: Display all saved contacts
- **Add Contact**: Create new contact entries with name and phone number
- **Edit Contact**: Update existing contact information
- **Delete Contact**: Remove contacts from your list
- **Search Contact**: Quickly find a specific contact by name
- **Persistent Storage**: All contacts are automatically saved to a JSON file

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd contact
   ```

## Usage

Run the program using Python:

```bash
python contact.py
```

### Menu Options

When you run the program, you'll see the following menu:

```
--- CONTACT BOOK ---
1. View Contacts
2. Add Contact
3. Edit Contact
4. Delete Contact
5. Search Contact
6. Exit
```

Simply enter the number corresponding to your desired action.

### Examples

**Adding a Contact:**
```
Choose option: 2
Enter name: John Doe
Enter number: 555-1234
Contact added!
```

**Searching for a Contact:**
```
Choose option: 5
Search name: John Doe
John Doe : 555-1234
```

**Editing a Contact:**
```
Choose option: 3
Enter contact name to edit: John Doe
Enter new number: 555-5678
Contact updated!
```

## Data Storage

Contacts are automatically saved to `contacts.json` in the same directory as the script. The file is created automatically on first use and updated with each modification.

## Project Structure

```
contact/
├── contact.py       # Main application file
├── contacts.json    # Auto-generated contact storage (created after first use)
└── README.md        # This file
```

## Functions Overview

- `load_contacts()`: Loads contacts from the JSON file
- `save_contacts()`: Saves contacts to the JSON file
- `show_contacts()`: Displays all contacts
- `add_contact()`: Adds a new contact
- `edit_contact()`: Modifies an existing contact
- `delete_contact()`: Removes a contact
- `search_contact()`: Finds a specific contact
- `main()`: Main program loop with menu interface

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.
