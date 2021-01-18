import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 195)


def talk(text):
    engine.say(text)
    engine.runAndWait()


flag = 0


def take_command():
    global flag
    try:
        with sr.Microphone() as source:
            flag = 0
            print('Sid wakes up...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'bot' not in command:
                flag = 1
            else:
                    command = command.replace('bot', '')

    except sr.UnknownValueError:
        flag = 1
    except sr.RequestError:
        flag = 1
    except LookupError:
        flag = 1
    return flag, command


def sent_msg():
    talk('Tell me the message')
    flag, comm = take_command()
    msg = comm
    print(msg)
    talk('Tell me the number')
    flag, comm = take_command()
    num = comm
    n = num.replace(' ', '')
    print(n)
    talk('Tell me the hour in 24 hour format')
    flag, comm = take_command()
    hr = comm
    h = hr.replace(' ', '')
    print(h)
    talk('Tell me the minutes')
    flag, comm = take_command()
    mi = comm
    m = mi.replace(' ', '')
    print(m)
    pywhatkit.sendwhatmsg("+91" + num, msg, int(h), int(m))
    return flag


def run_sid():
    global flag
    flag, command = take_command()
    if flag == 1:
        flag=1
    else:
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            print('playing ' + song)
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            flag = 1
        elif 'send' in command:
            sent_msg()
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            dat = datetime.datetime.now().strftime('%G:%A:%d')
            print(dat)
            talk(dat)
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        else:
            talk('I didnt understand,Please say the command again.')
    return flag


while True:
    flag, command = take_command()
    flag = run_sid()
    if flag == 1 or flag == 1:
        break
    else:
        run_sid()