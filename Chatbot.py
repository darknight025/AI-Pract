
import random

# Define responses to general queries
general_responses = [
    "Hello! How can I assist you today?",
    "Hi there! What can I help you with?",
    "Hey! Feel free to ask me anything.",
    "Greetings! What do you need help with?",
    "Hello, how may I be of service to you?"
]

# Define responses to specific questions
specific_responses = {
    "What is your name?": "I am a chatbot designed to assist you. You can call me ChatBot!",
    "How are you?": "As an AI, I don't have feelings, but I'm here and ready to help!",
    "What is the meaning of life?": "The meaning of life is subjective and varies from person to person.",
    "Can you tell me a joke?": "Why don't scientists trust atoms? Because they make up everything!",
    "Who created you?": "I was created by a team of developers at OpenAI.",
    "What is the weather like today?": "I'm sorry, but I'm not capable of providing real-time information like the weather.",
    "What can you do?": "I can answer your questions, tell you jokes, and provide general assistance.",
    "Do you have any hobbies?": "I'm an AI, so I don't have hobbies in the same way humans do, but I enjoy helping users like you!",
    "How old are you?": "I don't have an age since I'm an artificial intelligence program.",
    "Where do you live?": "I exist in the digital realm, so you can find me wherever you have access to the internet!",
    "Can you sing?": "I can't sing, but I can definitely assist you with information and tasks!",
    "What is your favorite color?": "As an AI, I don't have preferences like humans do.",
    "Do you dream?": "No, I don't dream. I'm always here and ready to assist you whenever you need help!"
}

def chatbot_response(user_input):
    if user_input in specific_responses:
        return specific_responses[user_input]
    else:
        return "I may not able to answer this question"

# Main function to interact with the chatbot
def main():
    print("Welcome to the ChatBot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip().capitalize()
        
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
