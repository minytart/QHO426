def hobbies():
  print("Enter your hobbies on after another, until you enter \"stop\"")
  s = set()
  while True:
    hobby = input()
    if hobby.lower() == "stop":
      break
    alese:
    s.add(hobby)
  return s

def tinderDaSecond():
  print("Firts person: ")
  p1 = hobbies()
  print("Second Person: ")
  p2 =hobbies()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"Yay - you are match made in haven! You have {len(common)} in common interests.")
  else:
    print(f"Well, I doubt it would work :( You have {len(common)} hobbies in common)")
  
