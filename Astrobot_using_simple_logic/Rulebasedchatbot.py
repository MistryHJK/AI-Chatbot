# Description: This is a simple rule-based chatbot that can respond to a few simple questions and statements.
import re # Regular Expression
import random 

#Define Rules
class Rulebasedchatbot:
    def __init__(self):
        self.rules = {
            r"how are you doing|how are you|how's it going": "I'm just a bunch of code, but I'm doing great! How about you?",
            r"what is your name|who are you": "I am a Rule-based Chatbot. You can call me 'Chatty'.",
            r"bye|goodbye|see you": "Goodbye! Don't forget to smile today!",
            r"exit|quit|end": "Exiting now! Catch you later, alligator! 🐊",
            r"what is (your|my) favorite color": "I don't have a favorite color, but I like all the colors of the rainbow... even the ones that don't exist!",
            r"what is the meaning of life": "The meaning of life is... 42! Wait, wrong answer... or maybe not? 😉",
            r"are you real": "I'm as real as your Wi-Fi connection... which can sometimes be a bit spotty.",
            r"do you love me|am I your friend": "Of course! You're my favorite human (but don't tell the others)!",
            r"hi|hello|hey|yo": "Hello! How can I assist you today?",
            r"tell me a joke|joke|make me laugh": self.get_joke,
    }
# Define Functions        
    def get_joke(self):
        jokes = [
                "Why don't scientists trust atoms?\n Because they make up everything.",
                "\nWhy don't eggs tell jokes?\nThey'd crack each other up.\n", 
                "Why did the scarecrow win an award?\n Because he was outstanding in his field.\n",
                "What do you call a fake noodle?\nAn im pasta.\n", 
                "Why did the bicycle fall over?\n Because it was two-tired."
            ]
        
        return random.choice(jokes)
# Chat Function    
    def chat(self):
        print("I am Your Astro Chatbot, Ask me anything: ")
        while True:
            user_input = input("You: ").lower()
            response = self.get_response(user_input)
            print("Chatbot: ",response)
            if "exit" in user_input or "quit" in user_input or "q" in user_input or "!q" in user_input:
                break
 # Get Response Function           
    def get_response(self, user_input):
        for pattern, response in self.rules.items():
            if re.search(pattern,user_input,re.IGNORECASE):
                if callable(response):
                    return response()
                return response
        else:
            print("Sorry:( I dont have any idea ")
                
if __name__ == "__main__":
    chatbot = Rulebasedchatbot()
    chatbot.chat()