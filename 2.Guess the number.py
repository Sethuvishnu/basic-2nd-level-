import random
def guess(x):
  random_int=random.randint(1,x)
  guess=0
  while guess != random_int:
    guess=int(input(f"enter from 1 to {x}:"))
    if guess < random_int:
      print("too low")
    elif guess >random_int:
      print("too far")
  print(f"crt, number is {random_int}")

guess(10)


