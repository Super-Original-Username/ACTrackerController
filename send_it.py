import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import os


class send_it():

    def __init__(self, IMEI, from_addr, to_addr, passwd):
        self.IMEI = IMEI
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.passwd = passwd

    def cutdown(self):
        self.send('cut')

    def idle(self):
        self.send('idle')

    def open_valve(self):
        self.send('open')

    def close_valve(self):
        self.send('close')

    def send(self, cmd):
        if cmd == 'cut':
            fileOut = ""  # This will link to the cutdown command file
        if cmd == 'idle':
            fileOut = ""  # This will link to the idle command file
        if cmd == 'open':
            fileOut = ""  # Valve opener file
        if cmd == 'close':
            fileOut = ""  # Valve closer file

        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = self.to_addr
        msg['Subject'] = self.IMEI
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(cmd, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filname=%s' % cmd)
        body = ""
        msg.attach(MIMEText(body, "plain"))
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.from_addr, self.passwd)
        text = msg.as_string()
        server.sendmail(self.from_addr,self.to_addr,text)