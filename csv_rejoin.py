import csv
if __name__=="__main__":
    with open("fee.csv", "r") as infile, open("fee1.csv","w+") as outfile:
        reader = csv.reader (infile)
        for row in reader:
            outfile.write('{}\n'.format(" ".join(row)))

    with open("fee1.csv","r") as csvfile:
        exp = []
        for row in csv.reader(csvfile, delimiter=' '):
            exp.append(float(row[1]))

        print (sum(exp))



