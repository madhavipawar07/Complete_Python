import pyttsx3

engine = pyttsx3.init()

students = ["Amit", "Priya", "Rahul", "Sneha", "Ritika", "Deepika", "Madhavi"]

speech = "Let us give a big shoutout to our amazing students. "

for name in students:
    speech += f"Congratulations {name}. "

speech += "Well done everyone."

engine.say(speech)
engine.runAndWait()