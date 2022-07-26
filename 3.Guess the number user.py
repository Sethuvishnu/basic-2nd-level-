import random
def com_guess(x):
  high=x
  low=1
  feedback=""
  while feedback!="c":
    if high!=low:
      guess=random.randint(low,high)
    else :
      guess=low
    feedback=input(f"is {guess} is high(h) or low(l) or crt(c)")
    if feedback=="h":
      high=guess-1
    elif feedback=="l":
      low=guess+1
  print(f"crt number is {guess}")
com_guess(10)