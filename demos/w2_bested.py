salary = float(input("What is your salary? "))
years = int(input("How long have you worked for me? "))

if years > 2:
  if salary < 25000:
    salary = salary*1.1
    print(f"Your new salary will be ${salary: .2f}")
  else:
    salary = salary + 100
    print(f"Small change. Now you gate ${salary: .2f} ")
elif years >= 1:
  print("No salary increase for you. Sorry :(")
else:
  if salary < 15000:
    print("oopsie, it's am error. You wil earn 20000")
    salary = 20000
print("Let's work hard")