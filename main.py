import speech_recognition as s_r
import pyttsx3


print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()


my_mic = s_r.Microphone(device_index=1) 

with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone


engine = pyttsx3.init()

try:
    text = r.recognize_google(audio)
except s_r.UnknownValueError:
    text = "Sorry, I could not understand your speech"
engine.say(text)

engine.runAndWait()


