# Simple Calculator

A command-line calculator application built with Python that performs basic arithmetic operations.

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division error handling)
- **Interactive Menu**: User-friendly command-line interface
- **Input Validation**: Handles invalid inputs gracefully

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd calculator
```

2. No additional dependencies required - uses only Python standard library

## Usage

Run the calculator:
```bash
python calculator.py
```

### Example

```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Enter choice (1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## How It Works

The calculator provides a continuous loop that:
1. Displays a menu of operations
2. Accepts user input for operation selection
3. Prompts for two numbers
4. Performs the selected operation
5. Displays the result
6. Repeats until the user chooses to exit

## Error Handling

- **Division by Zero**: Returns an error message instead of crashing
- **Invalid Input**: Catches non-numeric inputs and prompts the user to try again
- **Invalid Menu Choice**: Alerts the user to select a valid option (1-5)

## License

This project is open source and available for educational purposes.
