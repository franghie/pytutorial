inchars = "abcdefghijklmnopqrstuvwxyz"
outnchars = "cdefghijklmnopqrstuvwxyzab"

trans = str.maketrans(inchars, outnchars)

url = "map"

result = url.translate(trans)
print (result)