import re

#  start/end ^ $
#  dot, \d, \w, [A-Z], [a-z], \s
#  ? * +  {m} {m,n}
# ()

#  re.search
#  re.match

with open ("ch4.txt") as f:
    data = f.read()

result = re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]",data)

print (result)

for x in result:
    print(x, "-", x[4])

#print("".join([x[3] for x in result]))

#