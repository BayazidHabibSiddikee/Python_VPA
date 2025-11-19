# -*- coding: utf-8 -*-
"""
Batch Email Sender - smtplib with UTF-8 MIME
"""
import smtplib, time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipients, subject, body):
    sender = "pythonlusty@gmail.com"
    password = os.getenv("EMAIL_PASSWORD", "svzctudsgjvtffde")  # fallback for demo

    # Build MIME message with UTF-8 encoding
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipients if isinstance(recipients, str) else ", ".join(recipients)
    msg["Subject"] = subject

    # Attach body as UTF-8 plain text
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipients, msg.as_string())
        print(f"Email sent successfully to {recipients}")
        server.quit()
    except Exception as e:
        print(f"Email could not sent to {recipients}")
        print(f"Error: {e}")


# Example recipient list
recipients = [f"{i}@student.ruet.ac.bd" for i in range(2208001, 2208061)]
print(f"Sending email to {recipients}")

subject = "Special Discount on Our New Hoodie — Limited offer for MTE-22"
body = """Hello there,

We’re excited to introduce our new premium hoodie built with comfort, style, and long-lasting quality.
To celebrate the launch, we’re giving an exclusive limited-time discount to our email subscribers!

Special Offer Just for You MTE-22 By Roudrik: https://www.facebook.com/share/p/17QEioLFeS/

Premium comfort
Unique design
Perfect for winter
Available in all sizes
(Offer valid for a limited time 21 November 2025)

For you guys it's only 600/= TK BDT

Grab Yours Now
Order Now: https://docs.google.com/forms/d/e/1FAIpQLSfsnG3Y9UnSRsL6qFP06IVODMOdIi7rsy-ruzzuRqm9LUZkrQ/viewform?usp=dialog

Thank you for supporting us.
More exciting releases coming soon!

Warm regards,
roudrik

Check Out My YouTube Channel!: https://www.youtube.com/@mtemind
Don’t forget to subscribe for updates, behind-the-scenes content, and upcoming drops.
"""
for r in recipients:
    time.sleep(2)
    send_email(str(r), subject, body)
#send_email('2208053@student.ruet.ac.bd', subject, body)
