def  steps():
  likelihoods = ("step1", 50), ("step 2", 38), ("step3", 27), ("step 4", 99), ("step 5", 4)

def run():
  probabilities = steps()
  good_steps = []
  bad_steps = list()
  for tuplex in probabilities:
    if tuplex[1] >= 50:
      bad_steps.append(tuplex)
  else:
    good_steps.append(tuplex)
print("Good steps: {}, Bad setps: {}" .format(len(good_steps), len(bad_steps)))

run()