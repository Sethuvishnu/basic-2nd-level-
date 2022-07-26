import random
def play():
  user=input("rock,paper,scissors:  ")
  computer= random.choice(['r','p','s'])
  print(computer)
  if user==computer:
    return "tie"
  
  if win(user,computer):

    return 'you win'
  return 'you loose'
  




def win(player,opp):
  if(player=='r' and opp=='s') or (player=='s' and opp=='p') or (player=='p' and opp=='r'):
    return True
while True :

  print(play())
