matrix=[[1,2,3],[4,5,6]]
transposed = []
for i in range (3):
    transposed.append ([row[i] for row in matrix])
    print ([row for row in matrix])
    print ([row[i] for row in matrix])
    print transposed
print transposed

print ("--------------Transpoed 2------------------------")
transposed2=[[row[i] for row in matrix] for i in range (3)]
print transposed2
