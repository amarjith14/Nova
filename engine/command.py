import time
import pyttsx3
import speech_recognition as sr
import eel
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
    
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f'User said: {query}')
        #speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)
        
        

    except Exception as e:
        print(e)
        return ""
    
    return query.lower()

# text = takeCommand()

# speak(text)
@eel.expose
def allCommands():
    query = takeCommand()
    if not query:
        speak("Sorry, I didn't catch that.")
        return

    query = query.lower().strip()
    print(f"Final query: {query}")

    if 'open' in query:
        from engine.features import openCommand
        openCommand(query)

    elif 'on youtube' in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)

    elif 'system' in query and 'info' in query:
        from engine.features import getSystemInfo
        getSystemInfo()
        
    elif 'calendar' in query:
        from engine.features import showCalendar
        showCalendar(query)
        
    elif 'calculate' in query or ('what is' in query and any(op in query for op in ['+', '-', '*', '/', 'plus', 'minus', 'times', 'divided'])):
        from engine.features import calculate
        calculate(query)
        
    elif 'wikipedia' in query:
        from engine.features import searchWikipedia
        searchWikipedia(query)
        
    #elif (
     #   ("to do" in query or "todo" in query or "list" in query)
      #  and not ("show" in query or "mark" in query or "complete" in query)
    #):
     #   from engine.features import addTodo
      #  addTodo(query)

    #elif (
    #    ("show" in query or "display" in query or "list" in query)
    #    and ("to do" in query or "todo" in query or "tasks" in query)
    #):
     #   from engine.features import showTodoList
      #  showTodoList()

#    elif ('mark' in query or 'complete' in query) and ('task' in query or 'to do' in query):
 #       from engine.features import markTodoComplete
  #      markTodoComplete(query)

    elif 'remind me to' in query or 'set a reminder' in query:
        from engine.features import setReminder
        setReminder(query)
    

    elif any(kw in query for kw in ['news', 'headlines', 'get me the news', 'get me the news headlines', "today's news", 'latest headlines']):
        print(" Triggering getNewsHeadlines()")
        from engine.features import getNewsHeadlines
        getNewsHeadlines()


    elif 'time' in query:
        from engine.features import getTime
        getTime()
        
    
    elif 'call me' in query or 'my name is' in query:
        from engine.features import setUserName
        setUserName(query)
        
    elif 'who am i' in query or 'what is my name' in query:
        from engine.features import getUserName
        getUserName() 

    elif 'joke' in query or 'funny' in query or 'make me laugh' in query:
        from engine.features import tellJoke
        tellJoke()       

    
    
    elif 'date' in query or "today's date" in query or "what day is it" in query:
        from engine.features import getDate
        getDate()
    
    elif 'who are you' in query or 'introduce yourself' in query:
        from engine.features import introduceAssistant
        introduceAssistant()

    elif 'what can you do' in query or 'what are your capabilities' in query:
      speak("I can help you with various tasks like opening applications, playing videos on YouTube, telling jokes, getting news headlines, setting reminders, checking the time, and much more! Just ask.")
    
            
    else:
        speak("I'm not sure how to help with that yet.")
        print('Command not recognized')

    eel.ShowHood()

