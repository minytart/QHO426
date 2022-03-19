#Declare a tuple
p = ("Piotr", 88, False)
y = tuple([3, 6, 9])
#Print tuple
print(p)
print(y)
print(p[1])
print(y[0]*y[2])
#Cannot change values in a tuple => immutable
#y.append = 7778
#y.append(8)

#Concatenate tuples
z = p + y
print(z)
print(p)
print(y)

#Using minimum or maximum function
print(min(y))
print(max(y))