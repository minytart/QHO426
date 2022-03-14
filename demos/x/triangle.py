import random

def calc_area(h = 4, b = 6):
  area = h*b*0.5
  return area

def run():
  print(calc_area(random.randint(1, 10), 4))
  a1 = calc_area(18, 9)
  a2 = calc_area(2, 2)
  if a1>a2:
    print("Area 1 was larger")
  calc_area(100)
  calc_area(b=20)
  calc_area()