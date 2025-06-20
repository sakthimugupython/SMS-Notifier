# 📲 SMS Notifier – Python + Twilio API

A simple command-line tool that sends SMS messages using the **Twilio API**. Useful for alerts, notifications, or simple automation scripts.

---

## ✅ Features

- Send SMS messages to any phone number
- Uses Twilio's REST API (via `twilio` Python library)
- Clean command-line interface
- Includes support for **Twilio trial account limitations**

---

## 🧰 Requirements

- Python 3.6+
- Twilio account (Free or Paid)

### Install dependencies:

```bash
pip install twilio
🔑 Twilio Setup
Create a free account: https://www.twilio.com/try-twilio

Get your:

Account SID

Auth Token

Twilio phone number (starts with +1... or another region)

If you're on a trial account, you must verify recipient numbers manually:

Go to Verified Caller IDs

Add your phone number

Confirm using the code sent via SMS or call

📁 Example Code Structure
bash
Copy
Edit
sms_notifier.py      # Main script
README.md            # Documentation
🚀 Usage
1. Update Configuration in sms_notifier.py
python
Copy
Edit
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
twilio_number = '+1234567890'  # Your Twilio phone number
💡 For security, use environment variables or a .env file in production.

2. Run the script
bash
Copy
Edit
python sms_notifier.py
3. Input example:
mathematica
Copy
Edit
📱 Enter recipient number (e.g., +91xxxxxxxxxx): +919876543210
📝 Enter your message: Hello from Python!

✅ SMS sent! Message SID: SMxxxxxxxxxxxxxxxxxx