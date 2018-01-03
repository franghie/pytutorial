import zipfile , re
import string

num = "90052"
f = zipfile.ZipFile("/home/samuel/Downloads/channel.zip")
comments = []
while True:
    content = f.read(num + ".txt")
    # print(str(content))
    nums = re.findall("[0-9]+",str(content))
    comment = f.getinfo(num + ".txt").comment
    print (comment)
    comments.append((comment).decode())
    # print (nums)
    if (nums is None or len(nums) == 0):
        break
    num = nums[0]
    print (content)
print ("".join(comments))
print (set(comments))

# http://www.pythonchallenge.com/pc/def/oxygen.html
