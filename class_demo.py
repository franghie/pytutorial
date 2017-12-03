# In dictionary, key can be anything but should be unique. For class __dict__ is a dictionary, with variable name as key, variable value as value
# In class, seft must be the first argument of any methods except static method, which is called as normal method
# Python has builtin variable for class and modules


import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, username, passwd):
        print("__init__")
        self.username = username
        self.passwd = passwd
        print(self.__dict__)

    def send(self, to, msg):
        s = smtplib.SMTP('localhost')
        s.sendmail(self.username, to, msg)
        s.quit()
        self.new1 = "new1"
        print (self.__dict__)

    def add(self, short, long, dest, default, help):
        self.__dict__[dest] = default

    @staticmethod
    def hello(msg):
        print("hello " + msg)


EmailSender.hello("world")

sender = EmailSender("xiangxia.sun@gmail.com", "sunie3651224")
print(sender.username)
print(sender.passwd)

sender.add("-n", "--samuel", dest="xiaobing", default=100000,  help="samuel salary")
sender.add("-s", "--sunny", dest="lingdao", default=90000,  help="samuel salary")
print(sender.xiaobing)
print(sender.lingdao)
try:
    print(sender.xiaobingaaaaaaaa)
except:
    pass

sender.send("zhifan.nie@gmail.com", "python: email sender demo")
print (sender.__dict__)
