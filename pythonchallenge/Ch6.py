import pickle, urllib
from urllib import request

url = "http://www.pythonchallenge.com/pc/def/banner.p"
pickle_file = urllib.request.urlopen (url)
content = pickle.load(pickle_file)
print (content)
for row in content:
    print ("".join([t[0]*t[1] for t in row]))

# http://www.pythonchallenge.com/pc/def/channel.html