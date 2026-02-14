import json

FILE_NAME = "library.json"


class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available
        }


def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def show_books(books):
    if not books:
        print("\nNo books in library.")
        return

    print("\n--- LIBRARY BOOKS ---")
    for b in books:
        status = "Available" if b["available"] else "Borrowed"
        print(f"{b['title']} by {b['author']} - {status}")


def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author: ")

    book = Book(title, author)
    books.append(book.to_dict())
    save_books(books)
    print("Book added!")


def borrow_book(books):
    title = input("Enter book title to borrow: ")

    for b in books:
        if b["title"].lower() == title.lower():
            if b["available"]:
                b["available"] = False
                save_books(books)
                print("Book borrowed successfully!")
            else:
                print("Book already borrowed!")
            return

    print("Book not found!")


def return_book(books):
    title = input("Enter book title to return: ")

    for b in books:
        if b["title"].lower() == title.lower():
            b["available"] = True
            save_books(books)
            print("Book returned!")
            return

    print("Book not found!")


def search_book(books):
    keyword = input("Enter title to search: ").lower()

    found = False
    for b in books:
        if keyword in b["title"].lower():
            status = "Available" if b["available"] else "Borrowed"
            print(f"{b['title']} by {b['author']} - {status}")
            found = True

    if not found:
        print("No matching books found.")


def main():
    books = load_books()

    while True:
        print("\n--- LIBRARY SYSTEM ---")
        print("1. View Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            search_book(books)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


main()
