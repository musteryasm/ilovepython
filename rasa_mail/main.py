from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib

class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        recipient_email = tracker.latest_message['text']  # Extract email from user's message

        # Compose the email
        subject = "Your subject here"
        message = "Your email message here"

        # Connect to Gmail's SMTP server and send the email
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("sm@gmail.com", "password")
            server.sendmail("shivammusterya@gmail.com", recipient_email, f"Subject: {subject}\n\n{message}")
            server.quit()
            dispatcher.utter_message("Mail Sent")
        except Exception as e:
            dispatcher.utter_message(f"Failed to send email: {str(e)}")

        return []
