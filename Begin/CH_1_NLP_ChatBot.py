from textblob import TextBlob

intents = {
    "hours":{
        "keywords":["hours", "open", "close"],
        "response": "We are open from 9 AM to 5 PM Monday to Friday."
    },
    "return":{
        "keywords":["refund", "money back", "return"],
        "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}
# Define intents and their corresponding responses based on keywords

    # Convert the message to lowercase for consistent keyword matching
  
    # Check if the message contains any keywords associated with defined intents
    
    
    # Analyze the sentiment of the message using TextBlob

    
    # Return a response based on the sentiment score
   
def get_response(message):
    message = message.lower()
    if any(word in message for word in intents["keywords"]):
        return intents["response"]
        sentiment = TextBlob(message).sentiment.polarity
    return ("That's great to hear" if sentiment > 0 else
            "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
            "I see. Can you tell me more about that?")
 # Greet the user and prompt for input
   
    # Continuously prompt the user for input until they choose to exit
   
    # Thank the user for chatting when they exit

def chat():
    print("Chatbot: Hi how can I help you today?")
    while(user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")
    print("ChatBot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    chat()  # Start the chat when the script is executed
