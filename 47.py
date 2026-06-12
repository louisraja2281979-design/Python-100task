import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail account
sender_email = "your_email@gmail.com"
app_password = "your_app_password"

# Email details
subject = "Test Bulk Email"
message_body = """
Hello,

This is a bulk email sent using Python.

Thank you.
"""

# Read recipient emails
with open("emails.txt", "r") as file:
    recipients = [line.strip() for line in file if line.strip()]

# Connect to Gmail SMTP
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

# Send emails
for recipient in recipients:
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(message_body, "plain"))

        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    except Exception as e:
        print(f"Failed to send to {recipient}: {e}")

server.quit()
print("Done!")