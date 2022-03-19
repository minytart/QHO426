#Python program to get average of a list

def Average(list):
  return sum(list) / len(list)

#Driver ode

list =[15, 9, 55, 41, 99, 29, 62, 49]
average = Average(list)

#Printing average of the list
print("Average =", round(average, 2))