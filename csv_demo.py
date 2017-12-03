# import, function arguments(*args, *kwargs)
# csv, log, datetime, IO, print, built-in functions
# dictionary, list, string, tuple, int, float
# class
# value, reference


import csv

if __name__ == "__main__":
    with open("demo.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['date'], row['library'])

    # c-style
    with open("fee.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        total = 0
        for row in reader:
            total = total + float(row[1])
        print (total)

    #vab-style
    with open("fee.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        exp = []
        for row in reader:
            exp.append(float(row[1]))
        total = sum(exp)
        print(total)


    #pythonic
    #list comprehension
    with open("fee.csv", "r") as csvfile:
        print(sum([float(row[1]) for row in csv.reader(csvfile)]))


