import smtplib
import logging

logging.basicConfig(filename="altar.log",format='%(asctime)s %(levelname)-8s %(message)s ',level=logging.INFO)

class emailsender:
    def __int__(self, username, password):
        self.username = username
        self.password = password


    def send (self, toAdd, msg):
        server = smtplib.SMTP('localhost')
        try:
            server.sendmail(self, toAdd, msg)
            logging.info("Email is sent successfully!")

        except:
            logging.error("Cannot send the email!")

        server.quit()