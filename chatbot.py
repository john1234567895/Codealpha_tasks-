# chatbot.py

def normalize(text):
    """Converts text to lowercase and removes extra spaces."""
    return text.strip().lower()

def load_responses():
    """Returns a dictionary of user inputs and predefined bot responses."""
    return {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a program, but I'm functioning as expected!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "what is your name": "I'm a simple chatbot created in Python."
    }

def get_bot_response(user_input, response_map):
    """Returns the appropriate response or a default reply."""
    user_input = normalize(user_input)
    return response_map.get(user_input, "I'm not sure how to respond to that.")

def start_chat():
    """Runs the chatbot in a loop until the user exits."""
    responses = load_responses()
    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input, responses)
        print("Chatbot:", response)
        
        if normalize(user_input) == "bye":
            break

# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    start_chat()