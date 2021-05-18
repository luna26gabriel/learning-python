import smtplib

sender = 'naoseimaseisso34@gmail.com'
reciver = 'gabrielluna2011002@gmail.com'
password = 'senhanaosei'
subject = 'Python email test'
body = 'I test i email'

#header
message = f"""From: Nsei{sender}
To: Nsei{reciver}
Subject: {subject}\n
{body}
"""

#server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged In...")

    server.sendmail(sender, reciver, message)
    print('Email has been send')
    
except smtplib.SMTPAuthenticationError:
    print('Unable to sign in')
