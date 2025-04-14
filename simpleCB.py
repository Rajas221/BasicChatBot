
def chatbot_response(user_input):
    user_input = user_input.lower()

    rules = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! How can I help you?",
        "how are you": "I'm just a program, but thanks for asking! How can I assist you?",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome! If you have more questions, feel free to ask.",
        "help": "Sure! What do you need help with?",
        "what is your name": "I'm a simple chatbot. You can call me Chatbot.",}
    
    for keyword in rules: 
        if keyword in user_input:
            return rules[keyword]
        
    return "I'm sorry, I don't understand that. Can you please rephrase?"

#Main Loop
def chat():
    print("Chatbot: Hello! I'm here to help you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

#start the chatbot 
if __name__ == "__main__":
    chat()
# This code implements a simple chatbot that responds to user input based on predefined rules.