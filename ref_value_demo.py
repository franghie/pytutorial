# All variable is a reference. In order to write a value, need to dereference. Scalar -> Need to use key or index

llist = [['a', 'b'], ['c'], ['d', 'e']]
for loc in llist:
    loc = ['a','b','c']
print(llist)

llist = [['a', 'b'], ['c'], ['d', 'e']]
for loc in llist:
    loc[0] = '1'
print(llist)

m = {'a':'1',
     'c':'2'}

lst = ['a', 'b', 'c']
for l in lst:
    l = '1'
print(lst)

lst = ['a', 'b', 'c']
for i in range(len(lst)):
    lst[i] =  '1'
print(lst)


dvalue = {
    "key1": "value1",
    "key2": 2
}

print(dvalue["key1"])
print(dvalue["key2"])
