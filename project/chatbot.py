def get_response(message):
    message = message.lower()

    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm doing great, thanks for asking!",
        "what is your name": "I am a simple Python chatbot.",
        "bye": "Goodbye! Have a nice day!",
        "help": "You can say hi, ask my name, or ask how I am."
    }

    for key in responses:
        if key in message:
            return responses[key]

    return "Sorry, I don't understand that."


def main():
    print("Chatbot started! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        reply = get_response(user_input)
        print("Bot:", reply)

        if "bye" in user_input.lower():
            break


main()
