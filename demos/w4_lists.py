#Declare an empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["Pizza", "Lasgna", "Spaghetti Bolognese"]
#Print entire list
print(yummy)
#Print single item
print(yummy[0])
#Print some elements
print(yummy[:2])
#Add elements to our list(expand it) - adding elements at the en of the list
print(bleh)
bleh.append("Fish")
bleh.append("Coconut")
bleh.append("Onion")
bleh.append("Chocolate")
print(bleh)
#Add multiple items to list, based on user input
n = int(input("How many add to add?"))
for i in range (n):
  yummy.append(input("Enter a new yummy food: "))
print(yummy)
#Addin data at any point inside of a list
print(bleh)
bleh.insert(1,"Mashed Potatoes")
print(bleh)
bleh.insert(3, "Cabbage")
print(bleh)
#Remove an item from list
if "Frankfurters" in bleh:
  bleh.remove("Frankfurters")
if "Pizza" in bleh:
  bleh.remove("Pizza")
print(bleh)
#Remove item via index
x = bleh.pop(2)
print(bleh)
print(x)
#Alternative way to delitin via index
del bleh[1]
print(bleh)
#Expending a list
print(yummy)
yummy.extend(["Fish", "Bacon", "Ketchup"])
print(yummy)
#Checking for a particular data type
lista = ["Fred", True, 6, 8, -7.88, False, "Lalala", 55]
total = 0
for item in lista:
  if isinstance(item, int):
    total += item
print(total)