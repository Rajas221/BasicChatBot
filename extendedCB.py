import re
import random
from datetime import datetime

#Rule based intetnts and responses

rules = {
    "Greeting": {
        "patterns": [r"hello\b", r"hi+\b", r"hey+\b"],
        "responses": ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Hey! What can I do for you?"]
    },
"How are you?": {
    "patterns": [r"how are you+\b", r"how's it going+\b"],
    "responses": ["I'm just a program, I am always good!", "Doing well, thank you! What about you?","Amazing! How can I assist you?"]
},
"Goodbye": {
    "patterns": [r"bye\b", r"goodbye\b", r"later\b"],
    "responses": ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Come back soon!"]
},
"Help" :{
    "patterns": [r"help\b", r"assist\b"],
    "responses": ["Sure! What do you need help with?", "I'm here to assist you! What do you need?"]
    }
}

# Function to get a response based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for intent, data in rules.items():
        for pattern in data["patterns"]:
            if re.search(pattern, user_input):
                return random.choice(data["responses"])
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"

#Save Conversations 
def log_conversation(user_input, response):
    with open("conversation_log.txt", "a") as f:
        f.write(f"{datetime.now()} - User: {user_input}\n")
        f.write(f"{datetime.now()} - Chatbot: {response}\n\n")

#Chatbot Main Loop

def chat():
    print("Chatbot: Hello! I'm here to help you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        log_conversation(user_input, response)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
# This code implements an extended chatbot that can handle multiple intents and log conversations to a file.