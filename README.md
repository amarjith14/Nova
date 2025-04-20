# 🧠 Nova - Your Personal Desktop Assistant

<<<<<<< HEAD
Nova is a smart, voice-powered desktop assistant built using Python. It can respond to your voice commands and help you with a variety of daily tasks such as setting reminders, checking the news, telling the time, and more.

## ✨ Features

- 🔊 Voice recognition and text-to-speech
- 🕰️ Set and manage reminders (stored in a local SQLite database)
- 📰 Fetch latest news using NewsAPI
- ⏰ Tell the current time and date
- 🌐 Open websites and perform Google searches
- 📁 Launch local apps and files
- 📋 Perform sys
=======
Nova is a smart, voice-powered desktop assistant built using Python. It can respond to your voice commands and assist with various daily tasks such as setting reminders, checking the news, telling the time, launching apps, and more.

---
>>>>>>> 671eede451dc2cc1e24c4b2c8dfcf67fbaaa584d

## ✨ Features

<<<<<<< HEAD
## 🛠️ Tech Stack

- Python 3.10+
- `speech_recognition` for capturing voice input
- `pyttsx3` for text-to-speech
- `playsound` for audio notifications
- `sqlite3` for storing reminders
- `requests` for API calls (e.g., NewsAPI)
- `datetime` for date and time operations
=======
- 🔊 Voice recognition and text-to-speech
- 🕰️ Set and manage reminders (stored in a local SQLite database)
- 📰 Fetch latest news using NewsAPI
- ⏰ Tell the current time and date
- 🌐 Open websites and perform Google searches
- 📁 Launch local apps and files
- ⚙️ Perform system operations (shutdown, restart, etc.)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – for capturing voice input
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – for text-to-speech responses
- [`playsound`](https://pypi.org/project/playsound/) – for audio playback
- [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) – for local reminder storage
- [`requests`](https://pypi.org/project/requests/) – for API calls (e.g., NewsAPI)
- [`datetime`](https://docs.python.org/3/library/datetime.html) – for time/date functions

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/nova-desktop-assistant.git
cd nova-desktop-assistant
```
>>>>>>> 671eede451dc2cc1e24c4b2c8dfcf67fbaaa584d

2. **Install required packages:**

<<<<<<< HEAD
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
=======
```bash
pip install -r requirements.txt
```

3. **Add your API keys:**

Create a `.env` file or modify the relevant section in your code:

```python
NEWS_API_KEY = 'your_newsapi_key_here'
```

4. **Run Nova:**

```bash
python main.py
```

---

## 🗣️ Example Commands

> Try speaking these to Nova:

- “What’s the time?”
- “Remind me to attend class at 10:00 AM”
- “Tell me the news”
- “Open YouTube”
- “Shut down the system”

---

## 📌 Notes

- Ensure your microphone is properly configured and accessible.
- Internet connection is required for online features like fetching news or searching Google.
- All reminders are saved locally using SQLite.
>>>>>>> 671eede451dc2cc1e24c4b2c8dfcf67fbaaa584d
