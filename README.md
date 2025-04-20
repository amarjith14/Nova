# 🧠 Nova - Your Personal Desktop Assistant

Nova is a smart, voice-powered desktop assistant built using Python. It can respond to your voice commands and help you with a variety of daily tasks such as setting reminders, checking the news, telling the time, and more.

## ✨ Features

- 🔊 Voice recognition and text-to-speech
- 🕰️ Set and manage reminders (stored in a local SQLite database)
- 📰 Fetch latest news using NewsAPI
- ⏰ Tell the current time and date
- 🌐 Open websites and perform Google searches
- 📁 Launch local apps and files
- 📋 Perform sys


## 🛠️ Tech Stack

- Python 3.10+
- `speech_recognition` for capturing voice input
- `pyttsx3` for text-to-speech
- `playsound` for audio notifications
- `sqlite3` for storing reminders
- `requests` for API calls (e.g., NewsAPI)
- `datetime` for date and time operations

### Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/nova-desktop-assistant.git
cd nova-desktop-assistant

2. **Install the required packages:**
pip install -r requirements.txt

3. **Add your API keys:**
NEWS_API_KEY = 'your_newsapi_key_here'

4. **Run Nova:**
python main.py


🗣️ Example Commands
"What’s the time?"

"Remind me to attend class at 10:00 AM"

"Tell me the news"

"Open YouTube"

"Shut down the system"
