#Instantiate empty dictionary
dicto = {}
d = dict()
#Instatiate non-empty dictionary
phonebook = {"Thomas":"0770123456", "Aga":"077321234", "Udoh":"0775464654"}
#print full dictionary
print(phonebook)
#print individual elements
print(f" Calling {phonebook['Aga']}")
#Zipping to list together
names = ["Jagoda", "Frank", "Ludovico"]
ages = [19, 72, 33]
people = dict(zip(names, ages))
print(people)
#traverse dictionary
for i in people:
  print(i)
for i in people.values():
  print(i)
for i,j in people.items():
  print(f"Person {i} is {j} years old")
