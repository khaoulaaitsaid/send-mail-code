from email.message import EmailMessage
import ssl
import smtplib

password = 'wryg sfst cbcs xkbd'
email_sender = 'khaoulagirl20@gmail.com'
email_password = password
email_receiver = 'nerige9608@getmola.com'

subject = "Learn how to send emails"
body = """
learn to send email with python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
