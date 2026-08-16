#Voice Assistant

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=5, phrase_time_limit=8)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower().strip()
            
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print("Command:", command)
                
    except sr.WaitTimeoutError:
        print("No speech detected")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Speech service error")
    except Exception as e:
        print("Error:", str(e))
        
    return command

def run_alexa():
    command = take_command()
    
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time_now}')

    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who is', '').replace('who the heck is', '').strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            print(info)
            talk(info)
        except:
            talk(f"Sorry, I couldn't find clear information about {person}")

    elif 'date' in command:
        talk("sorry, I have a headache")

    elif 'are you single' in command:
        talk("I am in a relationship with wifi")

    elif 'joke' in command or 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'search' in command or 'what is' in command or 'tell me about' in command:
        query = command.replace('search', '').replace('what is', '').replace('tell me about', '').strip()
        talk(f"Searching for {query}")
        pywhatkit.search(query)

    elif 'open' in command and 'website' in command:
        site = command.replace('open', '').replace('website', '').strip()
        talk(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")

    elif any(x in command for x in ['stop', 'exit', 'bye', 'goodbye', 'shut down', 'turn off']):
        talk("Goodbye! Have a nice day!")
        exit()

    else:
        talk(f"I don't know that one... but let me search for: {command}")
        pywhatkit.search(command)


print("Alexa is ready! Say 'alexa' followed by your command...")
talk("Hello boss! Alexa is online!")

while True:
    run_alexa()