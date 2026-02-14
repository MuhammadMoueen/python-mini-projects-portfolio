# Simple Python Chatbot

A simple command-line chatbot built with Python that responds to basic greetings and questions.

## Description

This is a beginner-friendly chatbot project that demonstrates basic natural language processing concepts using Python. The chatbot can recognize keywords in user input and provide appropriate responses.

## Features

- 🤖 Simple keyword-based response system
- 💬 Responds to common greetings and questions
- 🔄 Continuous conversation loop
- 🚪 Easy exit with "bye" command

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd project
```

2. No additional dependencies required - uses only Python standard library!

## Usage

Run the chatbot using Python:

```bash
python chatbot.py
```

### Example Conversation

```
Chatbot started! Type 'bye' to exit.

You: hi
Bot: Hello!

You: what is your name
Bot: I am a simple Python chatbot.

You: how are you
Bot: I'm doing great, thanks for asking!

You: bye
Bot: Goodbye! Have a nice day!
```

## Supported Commands

The chatbot recognizes the following keywords:
- `hi` - Greets you
- `hello` - Greets you
- `how are you` - Tells you how the bot is doing
- `what is your name` - Introduces itself
- `bye` - Exits the conversation
- `help` - Shows available commands

## How It Works

The chatbot uses a simple keyword matching system:
1. Converts user input to lowercase
2. Checks if any keywords are present in the message
3. Returns the corresponding response
4. If no keywords match, returns a default message

## Future Improvements

- [ ] Add more conversation topics
- [ ] Implement basic sentiment analysis
- [ ] Add conversation history
- [ ] Create a GUI interface
- [ ] Integrate with external APIs for weather, news, etc.

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is open source and available for educational purposes.

## Author

Created as a Python learning project.
