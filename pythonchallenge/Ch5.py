from urllib import request
import urllib,re

url_tmp = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
ref="66831"

for i in range(399):
    url = url_tmp.format(ref)
    response = urllib.request.urlopen(url)
    header = response.info()
    data = response.read()
    #print("response is:", response, " \n header is:", header, "\n data is: ", data)
    ref = re.findall("\d+",str(data))[0]
    print (url)


print ("url is:", url)

#http://www.pythonchallenge.com/pc/def/peak.html