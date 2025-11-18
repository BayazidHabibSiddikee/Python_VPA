# -*- coding: utf-8 -*-
"""
Simple Email Sender - Just smtplib
"""
import smtplib

# Your credentials
sender = "pythonlusty@gmail.com"
password = "ygszfsmeqplcfszd"

# Recipient
receiver = "bayazid11008@gmail.com"

# Email content
subject = "Test Email"
body = "Hello! This is a test email from Python."

# Combine into email format
message = f"Subject: {subject}\n\n{body}"

# Send email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")