print(__name__)
print("fibonacci importing")

#2, 3, 5, 8
def fibonacci(n):
    f = 1
    s = 1
    t = 1
    for i in range(n):
        t = f + s
        f = s
        s = t
    return t

print("fibonacci imported")

value = __name__

if __name__ == "__main__":
    print("fibonacci(1) = {}".format(fibonacci(1)))

