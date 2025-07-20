import pyttsx3
import speech_recognition as sr

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_and_convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("Request failed.")
            return ""

def generate_questions(resume_text):
    return [
        "Iam Prashu... AI..."
        "Tell me about yourself.",
        "What are your strengths?",
        "Tell me about your Family?",
        "What project you Done",
        "Explain About your project",
        "Ok.. You can leave thankyou..",
    ]

def conduct_interview(resume_text):
    questions = generate_questions(resume_text)
    for question in questions:
        speak_text(question)
        answer = listen_and_convert()
        print("Answer:", answer)
