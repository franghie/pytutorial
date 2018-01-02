# Html is a tree
# Send email six step : 1. set up sever 2 set up connecton ehlo 3.start tls 4. login 5. sendmail 6. quit
# MySQLdb fetchall returns iterable

import urllib
import datetime
from urllib import request
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import logging
import MySQLdb

logging.basicConfig(filename="altar.log",format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO)
class emailsender:
     def __int__(self):
         pass


     def send (self, fromAdd, password,toAdd,content):
         msg = MIMEText(content)
         msg['Subject'] = 'Temprature of HongKong'
         msg['From'] = fromAdd
         msg['To'] = ",".join(toAdd)

         server = smtplib.SMTP('smtp.gmail.com:587')
         server.set_debuglevel(True)
         server.ehlo()
         server.starttls()
         server.login(fromAdd, password)
         try:
             server.sendmail(fromAdd, toAdd, msg.as_string())
             logging.info("Email is sent successfully!")
         except:
             logging.error("Cannot send the email!")

         server.quit()


url = "http://www.hko.gov.hk/wxinfo/currwx/current.htm"
location = "Tseung Kwan O"
response = urllib.request.urlopen (url)
data = response.read()
soup = BeautifulSoup(data, "lxml")
#print (soup.prettify())
result = soup.find(text = location).parent

content = "Temprature of {} is: {}".format(datetime.date.today(),result.nextSibling)
print (content)

host = input ("Enter host ID:")
user = input ("Enter user ID:")
passwd = input("Enter the password: ")
print (host, user, passwd)

db = MySQLdb.connect (host,user,passwd,db = "DistributionList")
cursor = db.cursor()
cursor.execute("SELECT * FROM sender")
senderinfo = cursor.fetchall()[0]

fromAdd = senderinfo[0]
password = senderinfo[1]

cursor.execute ("SELECT emailaddress FROM recipient")
toAdd = [row[0] for row in cursor.fetchall()]


sender = emailsender()
sender.send(fromAdd, password,toAdd,content)