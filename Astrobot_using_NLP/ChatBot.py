import nltk
import random
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# download nltk libraries 
nltk.download('punkt')
nltk.download("wordnet")


class ChatBot:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

        # define some rules 
        self.rules = {
            "greeting": ["hi","hello","hey","yo"],
            "farewell": ["bye","goodbye", "see you", "exit", "quit", "catch me later"],
            "joke": ["tell me a joke","joke","make me laugh"],
            "name": ["What is your name", "who are you"],
            "how_are_you": ["how are you", "how are you doing"],
            "fav_color": ["what is your favorite color"],
            "meaning_of_life": ["what is the meaning of life"],
            "real": ["are you real", "do you exist"],
            "run": ["run","running","runs","runned"],
            "eat": ["eat","eats","eating","ate","eaten"],
            "work": ["work","works","worked","working"],
            "learn": ["learn","learns","learned","learning"],
            "python": ["python"]
        }

        self.response = {
            "greeting": ["hello! how can I assist today"],
            "farewell": ["GoodBye!! Don't forget to smile today!"],
            "joke": self.get_joke,
            "name": ["I am a chatBot, you can call me 'Chatty'"],
            "how_are_you": ["I am fine! what about you"],
            "fav_color": ["I dont have any fav color, but I like all color"],
            "meaning_of_life": ["The meaning of life is __ learning python"],
            "real": ["I am as real as your internet connection"],
            "run": ["I see you are talking and running, thats not good"],
            "eat": ["Eating is good for energy! dont use phone while eating"],
            "work": ["don't work just relax"],
            "learn": ["Everyday is an opprtunity to learn somehing new"],
            "python": ["python is not a snake, its a programming language"]
        }


    def get_joke(self):
        jokes = [
            "Teacher: Tum school kyun nahi aaye? \nStudent: Bird flu ho gaya tha. \nTeacher: Lekin ye to pakshiyon ko hota hai, insaanon ko nahi. \nStudent: Mujhe to wo bhi samjhaya tha, lekin mujhe yakeen hi nahi hua.",
            "Ek aadmi doctor ke paas gaya aur bola, 'Doctor sahab, mujhe bhoolne ki bimari ho gayi hai.' Doctor ne pucha, 'Kab se?' Aadmi bola, 'Kab se kya?'",
            "Patni (pati se): Kya tum mujhse pyaar karte ho? \nPati: Haan, bahut! \nPatni: Phir to hamesha mujhse yahi sawaal poochte rahoge.",
            "Baccha (pita se): Papa mujhe kyun tokte rehte ho? \nPita: Beta, tumhare paas sab kuch hai, phir bhi tum kyun pareshan ho? \nBaccha: Kyunki mujhe lagta hai ki main kho jaunga! 😂",
            "Teacher: Tum ghar kyun nahi gaye? \nStudent: Guruji, mere paas school ka kaam tha. \nTeacher: To tumne ghar par kyun nahi kiya? \nStudent: Mujhe laga school mein hi kar lunga."
        ]

        return random.choice(jokes)

    # lemmatization 
    def lemmatize(self, word):
        return self.lemmatizer.lemmatize(word, pos='v')

    # stemming 
    def stem(self, word):
        return self.stemmer.stem(word) 

    def process_input(self, user_input):
        # tokenization 
        # split the user input into words
        input_tokens = word_tokenize(user_input)

        # implement lemma
        lemma_input_tokens = [self.lemmatize(self.stem(word)) for word in input_tokens]

        for rules, phrases in self.rules.items():
            for phrase in phrases: 
                phrases_token = word_tokenize(phrase.lower())
                lemma_phrases_token = [self.lemmatize(self.stem(token)) for token in phrases_token]

                if set(lemma_phrases_token).issubset(set(lemma_input_tokens)):
                    return rules
                
    def get_response(self, user_input):
        rule = self.process_input(user_input)
        if rule in self.response:
            if callable(self.response[rule]):
                return self.response[rule]()
            return self.response[rule]
        return "Sorry, I dont understand that"


    def chat(self):
        print("hello I am your chatbot, please ask me anything")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ['exit',"quit","bye"]:
                print("ChatBot: GoodBye! see you soon!")
                break
            response = self.get_response(user_input)
            print(f'ChatBot: {response}')

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chat()