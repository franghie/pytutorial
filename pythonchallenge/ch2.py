
#s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
s = "map"

ls = len(s)
print(ls)
a = [ord(s[i]) for i in range(ls)]
print(a)
for i in range(ls):
    print(chr(a[i]) , chr(a[i]+2))
    if chr(a[i]) == "y":
        a[i] = "a"
    elif chr(a[i]) == "z":
        a[i] = "b"
    elif chr(a[i]) == " " or chr(a[i]) =="," or chr(a[i]) ==".":
        a[i] = chr(a[i])
    else:
        a[i] = chr(a[i] + 2)

print("".join(a))

# http://www.pythonchallenge.com/pc/def/ocr.html