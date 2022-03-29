#Initialise empty set
s = set()
s1 = {"Glarry", "Harry"}
#print(type (s1))
#Initialise non-empty set
colours = {"blue", "orange", "yellow", "purpule", "black"}
print(colours)
#Add elements to set
colours.add("white")
colours.add("red")
colours.add("green")
print(colours)
colours.add("orange")
colours.add("black")
print(colours)
#remove items from set
if "red" in colours:
  colours.remove("red")
if "Yellow" in colours:
  colours.remove("Yellow")
  print(colours)

#Checking membership
  col - input("Enter a colour")
if "blue" in colours:
  print("Yay -  my favorite colour")
else:
  prin("My colour is not there")


x = {"cyan", "purpule", "burgundy", "white", "green"}
#Union - joining two sets togheter, not keeping duplicates

c2 = colours.union(x)
print(c2)
print(x)
print(colours)

#interesction - looking at common elements

c3 = colours.intersection(x)
c4 = x.intersection(colours)
print(c3)

#Difference = keep only elements on one set, but not in the other

c4 = colours.difference(x)
c5 = x.difference(colours)
print(c4)
print(c5)




