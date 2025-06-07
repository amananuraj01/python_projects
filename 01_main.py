# Import necessary libraries
import speech_recognition as sr     # For speech to text
import webbrowser                   # To open websites
import pyttsx3                      # For text to speech

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process the given voice command
def processCommand(command):
    command = command.lower()  # Convert command to lowercase to handle variations

    # Check the command and open the respective website
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
    else:
        speak("Sorry, I didn't understand the command.")

# Main function
if __name__ == "__main__":
    speak("Initializing Jarvis...")  # Speak startup message

    # Run forever
    while True:
        try:
            # Use the microphone to listen for the trigger word "Jarvis"
            with sr.Microphone() as source:
                print("Say 'Jarvis' to activate...")
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                trigger = recognizer.recognize_google(audio)  # Convert voice to text

            # If the trigger word is "Jarvis", then ask for the next command
            if trigger.lower() == "jarvis":
                speak("Yes?")  # Acknowledge the user

                # Listen again for the actual command
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)  # Convert to text
                    print("You said:", command)
                    processCommand(command)  # Process the command

        # Handle common errors gracefully
        except sr.UnknownValueError:
            print("Didn't catch that.")  # When speech is not clear
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))  # API or internet issues
        except sr.WaitTimeoutError:
            print("Listening timed out.")  # When no speech is detected in time
        except Exception as e:
            print(f"Error: {e}")  # Other unknown errors
