import time
import sqlite3
import datetime
from plyer import notification

# Function to connect to the database
def connect_db():
    return sqlite3.connect('nova.db')

# Function to check for reminders
def check_reminders():
    while True:
        current_time = datetime.datetime.now().strftime('%I:%M %p')  # Get current time
        conn = connect_db()
        cursor = conn.cursor()
        
        # Fetch matching reminders
        cursor.execute("SELECT * FROM reminders WHERE strftime('%I:%M %p', reminder_time) = ?", (current_time,))
        reminders = cursor.fetchall()
        
        for reminder in reminders:
            task = reminder[1]
            reminder_time_str = datetime.datetime.strptime(reminder[2], '%Y-%m-%d %H:%M:%S').strftime('%I:%M %p')
            
            # Trigger a notification for the reminder
            notification.notify(
                title="Reminder",
                message=f"Task: {task} at {reminder_time_str}",
                timeout=10  # Notification duration in seconds
            )
            
            # Remove the reminder after it's triggered
            cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder[0],))
            conn.commit()
        
        conn.close()
        time.sleep(60)  # Check every minute

# Run the check_reminders function
if __name__ == "__main__":
    check_reminders()
