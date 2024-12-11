#!/usr/bin/python3
import smtplib, os, socket, pwd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class M365Mail:

    try:
        default_msg = (
        "No message provided...\n"
        "Gathered infos:\n"
        "Host: {host}\n"
        "User: {user}"
        ).format(host=socket.gethostname(), user=pwd.getpwuid(os.geteuid())[0])
        host = 'smtp.office365.com'
        port = 587
    except Exception as e:
        default_msg = f"No message provided Error gathering host/user info: {e}"


    def __init__(self, user, password, host=host, port=port):
        self.username = user
        self.password = password
        self.host = host
        self.port = port
        self.mail_from = user


    def send_mail(self, mail_to, subject, msg):
        if msg is None:
            msg = self.default_msg

        if isinstance(mail_to, list):
            mail_to = ", ".join(mail_to)

        mimemsg = MIMEMultipart()
        mimemsg['From']=self.mail_from
        mimemsg['To']=mail_to
        mimemsg['Subject']=subject
        mimemsg.attach(MIMEText(msg, 'html'))
        connection = smtplib.SMTP(host=self.host, port=self.port)
        connection.starttls()
        connection.login(self.username,self.password)
        connection.send_message(mimemsg)
        connection.quit()
