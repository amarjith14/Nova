# check_reminders.py

import time
import sqlite3
import datetime
from plyer import notification

# Connect to the database
def connect_db():
    return sqlite3.connect('nova.db')

def check_reminders():
    while True:
        now = datetime.datetime.now().strftime('%I:%M %p')
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT id, task, reminder_time FROM reminders")
        reminders = cursor.fetchall()

        for rid, task, reminder_time in reminders:
            try:
                # Parse time and compare
                rt = datetime.datetime.strptime(reminder_time, '%Y-%m-%d %H:%M:%S').strftime('%I:%M %p')
                if now == rt:
                    # Show notification
                    notification.notify(
                        title="🔔 Reminder",
                        message=f"{task}",
                        timeout=10
                    )
                    print(f"Reminder triggered: {task} at {rt}")
                    # Delete triggered reminder
                    cursor.execute("DELETE FROM reminders WHERE id = ?", (rid,))
                    conn.commit()
            except Exception as e:
                print("Reminder error:", e)

        conn.close()
        time.sleep(60)  # check every minute

if __name__ == "__main__":
    check_reminders()
