import random
import datetime

# Predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Namaste Nagu!"],
    "how_are_you": ["I'm doing great! How about you?", "Feeling awesome!"],
    "name": ["I am your Smart AI Assistant.", "You can call me PyAssistant!"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"],
    "joke": [
        "Why don’t programmers like nature? Too many bugs!",
        "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep!'"
    ]
}

def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {now}"

def get_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    return f"Today's date is {today}"

def get_intent(user):
    user = user.lower()

    if any(word in user for word in ["hi", "hello", "hey"]):
        return "greeting"
    if "how are" in user:
        return "how_are_you"
    if "name" in user:
        return "name"
    if "bye" in user:
        return "bye"
    if "time" in user:
        return "time"
    if "date" in user:
        return "date"
    if "joke" in user:
        return "joke"

    return "unknown"

def chatbot_reply(user_input):
    intent = get_intent(user_input)

    if intent in responses:
        return random.choice(responses[intent])

    if intent == "time":
        return get_time()

    if intent == "date":
        return get_date()

    return "I didn't understand that, but I'm learning!"

# Main loop
print("🤖 Smart AI Chatbot (Type 'exit' to stop)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Bot: Bye! Have a great day ❤️")
        break

    print("Bot:", chatbot_reply(user))
