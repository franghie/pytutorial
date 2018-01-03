from itertools import permutations
import urllib
from urllib import request

perms = ["".join(p) for p in permutations("air")]
print (perms)
for x in perms:
    try:
        response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/"+ x +".html")
        print(response.read())
    except:
        pass