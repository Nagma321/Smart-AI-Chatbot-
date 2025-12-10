import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-IN")
        print("You:", query)
    except:
        return "none"
    return query.lower()

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.date.today().strftime("%B %d, %Y")

def chatbot():
    speak("Hello Nagu! I am your advanced AI assistant. How can I help you?")

    while True:
        query = listen()

        if "none" in query:
            continue

        # greetings
        if "hello" in query or "hi" in query:
            speak("Hi Nagu! How are you?")

        # time
        elif "time" in query:
            speak(f"The time is {get_time()}")

        # date
        elif "date" in query:
            speak(f"Today's date is {get_date()}")

        # open sites
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # wikipedia search
        elif "search" in query:
            try:
                topic = query.replace("search", "")
                result = wikipedia.summary(topic, sentences=2)
                speak("Here is what I found:")
                speak(result)
            except:
                speak("Sorry, I couldn’t find that.")

        # jokes
        elif "joke" in query:
            speak("Why do Java developers wear glasses? Because they don't C sharp!")

        # stop chatbot
        elif "bye" in query or "stop" in query:
            speak("Goodbye Nagu! Have a wonderful day!")
            break

        else:
            speak("I didn’t understand that, but I'm learning!")

chatbot()
