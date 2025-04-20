import os
import eel
from engine.features import *
from engine.command import *
eel.init('www')

playAssistantSound()
eel.start('index.html', mode='chrome', host='localhost', port=8080, block=True)

import threading

import threading

# Start the reminder checking in a background thread
reminder_thread = threading.Thread(target=checkReminders)
reminder_thread.daemon = True
reminder_thread.start()
