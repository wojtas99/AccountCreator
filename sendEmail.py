import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Function that sends us the verification code
def sendMail(msgTo : str, msgCode : int):
    smtp_server = 'smtp.gmail.com'  # SMTP Server Address
    smtp_port = 587  # SMTP port
    smtp_username = 'xxxxx@gmail.com'  # Username SMTP
    smtp_password = 'xxxxxxxx'  # Password SMTP

    msg = MIMEMultipart()
    msg['From'] = smtp_username  # Message From
    msg['To'] = msgTo  # MessageTo
    msg['Subject'] = 'Verification Code'  #Subject of email

    message = 'Your Verification Code is ' + str(msgCode)
    msg.attach(MIMEText(message, 'plain'))

    # Inicjalization of connection with SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()