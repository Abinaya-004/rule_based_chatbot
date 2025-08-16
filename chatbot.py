import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import datetime

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize
lemmatizer = WordNetLemmatizer()
user_name = None

# Preprocessing function
def preprocess_input(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

# Intent matching
def get_response(user_input):
    global user_name
    lemmas = preprocess_input(user_input)

    # Greeting
    if any(word in lemmas for word in ['hi', 'hello', 'hey']):
        if not user_name:
            return "Hello! What's your name?"
        else:
            return f"Hi again, {user_name}! How can I help you?"

    # Set Name
    if "my" in lemmas and "name" in lemmas:
        name = user_input.split()[-1].capitalize()
        user_name = name
        return f"Nice to meet you, {name}!"

    if user_name is None and len(lemmas) == 1:
        user_name = user_input.capitalize()
        return f"Nice to meet you, {user_name}!"

    # Time
    if "time" in lemmas:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    # Date
    if "date" in lemmas:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}."

    # Mood
    if "sad" in lemmas:
        return f"I'm here for you, {user_name if user_name else 'friend'}. Want to talk about it?"
    if "happy" in lemmas:
        return "Yay! I'm glad to hear that 😊"

    # Goodbye
    if any(word in lemmas for word in ['bye', 'goodbye', 'see', 'later']):
        return f"Goodbye, {user_name if user_name else 'friend'}! Talk to you soon!"

    # Unknown
    return "Hmm, I didn't understand that. Can you say it differently?"

# Chatbot loop
def chatbot():
    print("🤖: Hello! I’m your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"🤖: {response}")
        if 'bye' in user_input.lower():
            break

# Run chatbot
chatbot()
