from datetime import datetime,date, timedelta
import calendar

#cal = calendar.month ( 2017, 12)
#print cal

d1 = date (2017,12,1)
d2 = date (2018,1,1)

bday = []
while d1 < d2:
    if  d1.weekday ()in range (5):
        bday.append (d1)
    d1 = d1 + timedelta (days = 1)

print "\n".join([d.strftime("%Y%m%d") for d in bday])

# lstr = ["a", "b", "c"]
# print "\n".join(lstr)
# print "<->".join(lstr)
# print ",".join(lstr)
