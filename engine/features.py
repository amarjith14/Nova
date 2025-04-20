import os
import re
import sqlite3
import webbrowser
from playsound import playsound
import eel

from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import datetime
import random
import os
import platform
import psutil
import wikipedia
import calendar
import pygame
from datetime import datetime
import time
import sqlite3
import requests


conn = sqlite3.connect("nova.db")
cursor = conn.cursor()
#sound function for playing sound
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

#click sound for mic button



@eel.expose
def playClickSound():
    music_file = "www/assets/audio/click_sound.mp3"
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Failed to play click sound: {e}")


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip().lower()

    if query != "":
        try:
            # Try to find the application in sys_command table
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
                return

            # If not found, try to find the URL in web_command table
            cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()
            
            if len(results) != 0:
                speak("Opening " + query)
                webbrowser.open(results[0][0])
                return

            # If still not found, try to open using os.system
            speak("Opening " + query)
            try:
                os.system('start ' + query)
            except Exception as e:
                speak(f"Unable to open {query}. Error: {str(e)}")

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I couldn't find what to play on YouTube.")


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None



# System information
def getSystemInfo():
    system_info = platform.uname()
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    
    info_text = f"System: {system_info.system} {system_info.release}\n"
    info_text += f"Processor: {system_info.processor}\n"
    info_text += f"CPU Usage: {cpu_usage}%\n"
    info_text += f"Memory Usage: {memory_info.percent}%"
    
    speak(f"Here's your system information:")
    speak(info_text)

# Calendar function
def showCalendar(query):
    try:
        # Extract month and year from query
        words = query.split()
        month_names = {
            'january': 1, 'february': 2, 'march': 3, 'april': 4,
            'may': 5, 'june': 6, 'july': 7, 'august': 8,
            'september': 9, 'october': 10, 'november': 11, 'december': 12
        }
        
        month = datetime.datetime.now().month  # Default to current month
        year = datetime.datetime.now().year    # Default to current year
        
        # Try to extract month and year from query
        for word in words:
            word = word.lower()
            if word in month_names:
                month = month_names[word]
            elif word.isdigit() and len(word) == 4:
                year = int(word)
        
        # Get calendar for the specified month and year
        cal = calendar.month(year, month)
        month_name = calendar.month_name[month]
        
        speak(f"Here's the calendar for {month_name} {year}")
        eel.DisplayMessage(cal)  # Display the calendar in the UI
        
    except Exception as e:
        speak(f"I couldn't show the calendar. Error: {str(e)}")

# Quick calculation
def calculate(query):
    try:
        # Extract the expression to calculate
        query = query.replace('calculate', '').strip()
        query = query.replace('what is', '').strip()
        
        # Handle basic calculations using eval() - be cautious with this in production!
        result = eval(query)
        speak(f"The result of {query} is {result}")
        
    except Exception as e:
        speak("I couldn't perform that calculation")

# Wikipedia search
def searchWikipedia(query):
    try:
        # Extract search term
        search_term = query.replace("wikipedia", "").replace("search", "").replace("for", "").strip()
        
        if search_term:
            speak(f"Searching Wikipedia for {search_term}...")
            results = wikipedia.summary(search_term, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        else:
            speak("What would you like me to search for on Wikipedia?")
    except Exception as e:
        speak("I couldn't find that information on Wikipedia")

# Simple to-do list functions
"""def addTodo(query):
    try:
        # Extract task
        task = query.replace("add to my to do list", "").replace("add to to do list", "").strip()
        
        if task:
            cursor.execute('CREATE TABLE IF NOT EXISTS todo_list (id INTEGER PRIMARY KEY, task TEXT, completed BOOLEAN)')
            cursor.execute('INSERT INTO todo_list (task, completed) VALUES (?, ?)', (task, False))
            conn.commit()
            speak(f"I've added '{task}' to your to-do list")
        else:
            speak("What task would you like me to add?")
    except Exception as e:
        speak(f"I couldn't add that to your to-do list. Error: {str(e)}")

def showTodoList():
    try:
        cursor.execute('SELECT id, task, completed FROM todo_list ORDER BY id')
        tasks = cursor.fetchall()
        
        if tasks:
            speak("Here's your to-do list:")
            task_list = ""
            for task_id, task, completed in tasks:
                status = "Done" if completed else "Not done"
                task_list += f"{task_id}. {task} - {status}\n"

            print("To-do list output:\n", task_list)  # ✅ Debug print
            eel.DisplayMessage(task_list)
            speak(f"You have {len(tasks)} items in your list")

        else:
            speak("Your to-do list is empty")
    except Exception as e:
        speak(f"I couldn't retrieve your to-do list. Error: {str(e)}") 

def markTodoComplete(query):
    try:
        # Extract task id or name
        words = query.split()
        task_id = None
        
        for word in words:
            if word.isdigit():
                task_id = int(word)
                break
        
        if task_id:
            cursor.execute('UPDATE todo_list SET completed = ? WHERE id = ?', (True, task_id))
            conn.commit()
            
            if cursor.rowcount > 0:
                speak(f"I've marked task {task_id} as complete")
            else:
                speak(f"I couldn't find task {task_id}")
        else:
            speak("Which task would you like to mark as complete?")
    except Exception as e:
        speak(f"I couldn't update your to-do list. Error: {str(e)}") """



# Reminder function (with time)
import sqlite3
import datetime
import sqlite3
import time
import datetime
from plyer import notification


# Function to connect to the nova.db database
def connect_db():
    conn = sqlite3.connect('nova.db')
    return conn

# Function to check for reminders
def checkReminders():
    while True:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reminders WHERE reminder_time = ?", (current_time,))
        reminders = cursor.fetchall()
        
        for reminder in reminders:
            task, reminder_time = reminder[1], reminder[2]
            speak(f"Reminder: {task} at {reminder_time.strftime('%I:%M %p')}")
            cursor.execute("DELETE FROM reminders WHERE reminder_time = ?", (current_time,))
            conn.commit()
        
        conn.close()
        time.sleep(60)  # Check every minute

def setReminder(query):
    try:
        # Extract time and task from query
        time_part = query.split('at')[-1].strip()
        task_part = query.split('to')[1].split('at')[0].strip()
        
        # Clean time part (standardize AM/PM)
        time_part = time_part.replace('p.m.', 'PM').replace('a.m.', 'AM')
        
        # Parse the time into datetime object
        reminder_time = datetime.datetime.strptime(time_part, '%I:%M %p')
        
        # Get today's date and combine it with the reminder time
        current_date = datetime.datetime.now().date()
        reminder_datetime = datetime.datetime.combine(current_date, reminder_time.time())
        
        # Store reminder in the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reminders (task, reminder_time)
            VALUES (?, ?)
        ''', (task_part, reminder_datetime))
        conn.commit()
        conn.close()
        
        # Send confirmation to the user
        speak(f"Reminder set: {task_part} at {reminder_datetime.strftime('%I:%M %p')}")
        print(f"Reminder set: {task_part} at {reminder_datetime.strftime('%I:%M %p')}")

    except Exception as e:
        print("Error setting reminder:", e)
        speak("Sorry, I couldn't understand the reminder format. Please try again.")


# News headlines (you would need a news API for a real implementation)

@eel.expose
def getNewsHeadlines():
    api_key = "4b4ce888d4944956927f207e714e28e1"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"


    print("Fetching news from:", url)

    try:
        response = requests.get(url)
        data = response.json()
        print("News API Response:", data)  # Debugging line

        if response.status_code == 200 and data.get('status') == 'ok':
            headlines = [article['title'] for article in data['articles'][:3]]
            if not headlines:
                speak("I couldn't find any news headlines right now.")
                eel.DisplayMessage("No news headlines found.")
                return

            for index, headline in enumerate(headlines, start=1):
                message = f"Headline {index}: {headline}"
                print(message)
                speak(message)
                eel.DisplayMessage(message)
        else:
            speak("Sorry, I couldn't fetch the news headlines now.")
            eel.DisplayMessage("Failed to get news. Please try again later.")
            print("News API response error:", data)
    except Exception as e:
        speak("Sorry, I couldn't fetch the news headlines now.")
        eel.DisplayMessage(f"Error fetching news: {str(e)}")
        print("News fetching error:", e)


# User name functions
def setUserName(query):
    # Extract name from command
    if "call me" in query:
        name = query.replace("call me", "").strip()
    else:  # "my name is" case
        name = query.replace("my name is", "").strip()
    
    if name:
        # Store user name in database
        try:
            cursor.execute('CREATE TABLE IF NOT EXISTS user_info (key TEXT PRIMARY KEY, value TEXT)')
            cursor.execute('INSERT OR REPLACE INTO user_info (key, value) VALUES (?, ?)', ('user_name', name))
            conn.commit()
            speak(f"I'll remember that your name is {name}")
        except Exception as e:
            speak(f"I couldn't save your name. Error: {str(e)}")
    else:
        speak("I didn't catch your name. Could you please try again?")

def getUserName():
    try:
        cursor.execute('SELECT value FROM user_info WHERE key = ?', ('user_name',))
        result = cursor.fetchone()
        
        if result:
            speak(f"Your name is {result[0]}")
        else:
            speak("I don't know your name yet. You can tell me by saying 'Call me' followed by your name.")
    except Exception as e:
        speak(f"I couldn't retrieve your name. Error: {str(e)}") 

def tellJoke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "What did the computer do at lunchtime? Had a byte!",
        "Why don't programmers like nature? It has too many bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
    ]
    selected_joke = random.choice(jokes)
    speak(selected_joke)        


# Time function
def getTime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Date function
def getDate():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")    

def introduceAssistant():
    speak(f"I am Nova, your personal desktop assistant. I can help you with various tasks like telling the time, date, opening applications, searching the web, and more.")
