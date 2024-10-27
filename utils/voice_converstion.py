import speech_recognition as sr
import time
import pyttsx3

class VoiceConversion:
    engine = pyttsx3.init()

    @staticmethod
    def listen():
        recognizer = sr.Recognizer()
        # Adjusting pause threshold to allow for natural pauses
        recognizer.pause_threshold = 1.0  # Increase pause time between words
        
        # Optionally adjust the energy threshold or use dynamic adjustment
        recognizer.energy_threshold = 400  # Sensitivity to background noise
        recognizer.dynamic_energy_threshold = True  # Dynamically adjust energy threshold based on ambient noise

        with sr.Microphone() as source:
            print("Listening for command... Take a deep breath and speak!")
            time.sleep(0.5)  # Small delay to give the user time to prepare
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
            return ""
        
    @staticmethod
    def speak(text):
        voices = VoiceConversion.engine.getProperty('voices')
        # index = 0
        # for voice in voices:
        #     print(f'index-> {index} -- {voice.name}')
        #     index +=1
        rate = VoiceConversion.engine.getProperty('rate')
        VoiceConversion.engine.setProperty('rate', rate-10)
        VoiceConversion.engine.setProperty('voice', voices[122].id)
        VoiceConversion.engine.say(text)
        VoiceConversion.engine.runAndWait()

# if __name__ == "__main__":
#     VoiceConversion.speak("Hello! I am ready to listen to your commands.")
#     while True:
#         command = VoiceConversion.listen()
#         if command == "exit":
#             VoiceConversion.speak("Exiting the program. Goodbye!")
#             break
#         elif command:
#             VoiceConversion.speak(f"You said: {command}")
