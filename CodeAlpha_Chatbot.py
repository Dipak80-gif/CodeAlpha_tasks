# Function to generate bot response
def chatbot_response(user_input):
    user_input = user_input.lower()   # convert input to lowercase
    
    if user_input == "hi":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, Thanks!"
    
    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that."


# Main chatbot function
def start_chat():
    print("Simple Chatbot (Type 'bye' to exit)")
    
    while True:  
        user_input = input("You: ")
        
        response = chatbot_response(user_input)  
        print("Bot:", response)
        
        if user_input.lower() == "bye":
            break  


# Run the chatbot
start_chat()
