with open ("ch3.txt") as f:
    data = f.read()
dict = {x:data.count(x) for x in set(data)}
sorted_dict = sorted (dict.items(), key = lambda x: x[1])

# print (sorted_dict)
for k, v in sorted_dict:
    print (k, v)


#http://www.pythonchallenge.com/pc/def/equality.html
