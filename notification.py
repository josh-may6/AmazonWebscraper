from email.message import EmailMessage
import smtplib


class Email:

    def __init__(self, price, link):
        self.my_email = "joshmaytree2@gmail.com"
        self.my_password = "mbsy irjh vyfs tlqi"  # This password you need two-step verification turned on Gmail. Create App Password
        self.msg = EmailMessage()
        self.msg["From"] = self.my_email
        self.msg["To"] = self.my_email
        self.msg["Subject"] = "🚨 Amazon Price Alert 🚨"
        self.msg.set_content(f"This product is only {price}! Click the link: {link}")

    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            connection.send_message(self.msg)
