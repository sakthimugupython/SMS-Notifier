from twilio.rest import Client

# account_sid = 'AC9d63142d4ac6d623b914bddac0f91548'
# auth_token = 'f0c5f9b4a92254fb6e6d1a94ebac2bc2'
# twilio_number = '+14845378950'

def send_sms(to_number, message_body):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=to_number
        )
        print(f"SMS sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

to = input("Enter recipient number (e.g., +91xxxxxxxxxx): ").strip()
msg = input("Enter your message: ").strip()
send_sms(to, msg)
