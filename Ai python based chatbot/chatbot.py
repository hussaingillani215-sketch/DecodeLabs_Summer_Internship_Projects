# Rule-Based AI Chatbot
# Project 1 - DecodeLabs Artificial Intelligence Internship
# Author: Syed Hussain Mohi ud Din Gillani
import string


def clean_text(user_input):
    """
    Cleans the user's input by:
    1. Converting it to lowercase
    2. Removing extra spaces
    3. Removing punctuation marks
    """

    user_input = user_input.lower().strip()

    # Remove punctuation like ?, !, ., commas, etc.
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces between words
    user_input = " ".join(user_input.split())

    return user_input


def get_response(user_input):
    """
    Matches the cleaned user input with predefined chatbot responses.
    Returns a suitable response based on rule-based logic.
    """

    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! Nice to meet you.",
        "hey": "Hey! How can I assist you?",
        "good morning": "Good morning! Hope you are having a great day.",
        "good evening": "Good evening! How can I help you?",

        "how are you": "I am doing great. Thank you for asking!",
        "how are you doing": "I am working perfectly and ready to help you.",
        "are you okay": "Yes, I am okay. Thanks for checking!",

        "what is your name": "My name is LogicBot, a rule-based AI chatbot.",
        "who are you": "I am a simple rule-based AI chatbot created using Python.",
        "what are you": "I am a chatbot that gives responses using predefined rules.",

        "what can you do": "I can answer simple questions based on predefined rules.",
        "help": "You can ask me: hello, how are you, what is your name, what can you do, or bye.",
        "features": "I can handle greetings, basic questions, unknown inputs, and exit commands.",

        "what is ai": "AI stands for Artificial Intelligence. It allows machines to perform tasks that normally require human intelligence.",
        "what is chatbot": "A chatbot is a program that can simulate conversation with users.",
        "what is rule based chatbot": "A rule-based chatbot follows fixed rules and gives predefined responses.",

        "thank you": "You are welcome!",
        "thanks": "No problem! Happy to help.",
        "okay": "Alright!",
        "ok": "Okay!"
    }

    exit_commands = ["bye", "exit", "quit", "stop", "goodbye", "see you"]

    if user_input == "":
        return "Please type something so I can respond.", False

    if user_input in exit_commands:
        return "Goodbye! Thanks for chatting with me.", True

    if user_input in responses:
        return responses[user_input], False

    return "Sorry, I do not understand that yet. Please try another question.", False


def chatbot():
    """
    Main chatbot function.
    Runs the chatbot in a continuous loop until the user enters an exit command.
    """

    print("Bot: Hello! I am LogicBot, your Rule-Based AI Chatbot.")
    print("Bot: Type 'help' to see what you can ask.")
    print("Bot: Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:
        user_input = input("You: ")

        cleaned_input = clean_text(user_input)

        response, should_exit = get_response(cleaned_input)

        print("Bot:", response)

        if should_exit:
            break


chatbot()