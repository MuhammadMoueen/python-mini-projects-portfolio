# Password Generator

A secure random password generator that creates strong passwords with letters, digits, and special characters.

## Features

- Generate random passwords of any length
- Combines uppercase letters, lowercase letters, digits, and punctuation
- Minimum password length validation (at least 4 characters)
- Simple command-line interface
- Continuous generation until user exits

## How It Works

The program uses Python's `random` and `string` modules to:
1. Create a pool of all possible characters (letters, digits, punctuation)
2. Randomly select characters to build a password of specified length
3. Return a secure, randomized password

## Usage

Run the program:
```bash
python password.py
```

Enter the desired password length when prompted, and the program will generate a secure password.

## Requirements

- Python 3.x
- No external libraries required (uses standard library only)

## Example

```
--- PASSWORD GENERATOR ---
Enter password length: 12
Generated Password: aB3#xM9$pL2@
```

## Password Strength Tips

- **Short (4-7 chars)**: Basic security, suitable for low-risk accounts
- **Medium (8-12 chars)**: Good security for most purposes
- **Long (13+ chars)**: Strong security for sensitive accounts
- **Very Long (20+ chars)**: Maximum security for critical systems

## Security Notes

- Generated passwords include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&* etc.)
- Each password is randomly generated
- Longer passwords are exponentially more secure
- Always store passwords securely (use a password manager)

## Character Set

The generator uses all printable ASCII characters:
- Letters: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Digits: `0123456789`
- Punctuation: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
