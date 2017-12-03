import argparse
from datetime import datetime, date, timedelta

parser = argparse.ArgumentParser (description= "Input a date and a number of days to find a business date after")
parser.add_argument ("-d", "--date", dest="start_date", help="Starting date")
parser.add_argument("-n", "--number",dest="delta",  help="number of days")
args = parser.parse_args()
start_date=datetime.strptime(args.start_date,"%Y,%m,%d")
i = int (args.delta)
#print (args.start_date, args.delta)
next_date=start_date
while i > 0:
    if next_date.weekday() in range (5):
       i=i-1;
    next_date = next_date + timedelta(days=1)

#friday 2
#saturday 1

print ("The business date your are looking for is: {}".format(datetime.strftime(next_date,"%Y,%m,%d")))





