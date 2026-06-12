from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Your approved WhatsApp sender number
FROM_WHATSAPP = "whatsapp:+14155238886"

# Recipient numbers
recipients = [
    "whatsapp:+911234567890",
    "whatsapp:+919876543210",
    "whatsapp:+918888888888"
]

message_text = "Hello! This is a bulk WhatsApp message sent using Python."

for recipient in recipients:
    try:
        message = client.messages.create(
            body=message_text,
            from_=FROM_WHATSAPP,
            to=recipient
        )
        print(f"Sent to {recipient}: {message.sid}")
    except Exception as e:
        print(f"Failed to send to {recipient}: {e}")