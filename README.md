# python_project1
Mega Project - Jarvis Virtual Assistance

This Python program is a basic **voice-activated virtual assistant named "Jarvis". It uses speech recognition and text-to-speech capabilities to interact with the user and perform web-based tasks.

 ✅ Key Features:

1. Voice Activation:

   * The assistant waits for the trigger word "Jarvis" to activate.

2. Speech Recognition:

   * Uses your microphone to listen and convert your spoken words into text using Google's speech recognition API.

3. Text-to-Speech (TTS):

   * Jarvis responds to your commands with spoken feedback using the `pyttsx3` TTS engine.

4. Web Navigation:

   * Can open popular websites like:

     * Google
     * YouTube
     * Facebook
     * Instagram

5. Continuous Listening Loop:

   * The program runs continuously, always ready to respond when it hears "Jarvis".

 🧠 **How It Works:**

* The program first listens for the trigger word **"Jarvis"**.
* Once triggered, it asks for your command.
* Based on your command, it opens the appropriate website in your default browser.
* If it doesn't recognize the command, it politely says so.

 🧰 Technologies Used:

* `speech_recognition` – For converting voice to text.
* `pyttsx3` – For converting text to speech.
* `webbrowser` – For launching websites.
* `sr.Recognizer()` and `sr.Microphone()` – To capture and process voice input.


