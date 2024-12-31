import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):

    machine.say(text)
    machine.runAndWait()

def input_instruction():
    
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "google" in instruction:
                print("Hello, you said:", instruction)
            return instruction
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
    except sr.RequestError as e:
        talk(f"Could not request results; {e}")
    except Exception as e:
        talk(f"An error occurred: {e}")
    return ""

def play_google():
    """Perform tasks based on voice commands."""
    while True:
        instruction = input_instruction()
        print("Instruction received:", instruction)

        if "play" in instruction:
            song = instruction.replace("play", "").strip()
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)
        elif "time" in instruction:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk(f"Current time is {time}")
        elif "date" in instruction:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            talk(f"Today's date is {date}")
        elif "search" in instruction:
            search = instruction.replace("search", "").strip()
            talk(f"Searching for {search}")
            pywhatkit.search(search)
        elif "tell me about" in instruction:
            topic = instruction.replace("tell me about", "").strip()
            talk(f"Let me tell you about {topic}")
            pywhatkit.search(topic)
        elif "joke" in instruction:
            talk("Here's a joke for you")
            pywhatkit.search("tell me a joke")
        elif "news" in instruction:
            talk("Here are some news for you")
            pywhatkit.search("latest news")
        elif "weather" in instruction:
            talk("Checking the weather for you")
            pywhatkit.search("current weather")
        elif "open" in instruction:
            app = instruction.replace("open", "").strip()
            talk(f"Opening {app}")
            os.system(f"start {app}")
            # Replace with actual paths to your apps
            try:
                os.startfile(app)
            except FileNotFoundError:
                talk("Sorry, I couldn't find the application.")
        elif "exit" in instruction:
            talk("Goodbye!")
            break
        else:
            talk("I didn't understand that. Can you repeat?")

# Start the assistant
play_google()
