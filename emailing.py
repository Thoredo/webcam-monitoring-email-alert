import smtplib
import imghdr
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
SENDER = os.getenv("MY_EMAIL")
RECEIVER = os.getenv("MY_EMAIL")

def send_email(image):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")
    
    with open (image, "rb") as file:
        content = file.read()
    
    email_message.add_attachment(content, maintype="image", 
                                 subtype=imghdr.what(None, content))
    
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image="images/image_20.png")