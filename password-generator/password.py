import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""  # Default password

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("\n--- PASSWORD GENERATOR ---")
    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password should be at least 4 characters!")
                return

            password = generate_password(length)
            print("Generated Password:", password)

        except:
            print("Please enter a valid number!")


main()
