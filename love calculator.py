
t=r=u=e=l=o=v=e=''

name1=input("enter 1st name: ")
name2=input("enter 2nd name: ")
combine=name1+name2

t=combine.count('t')
r=combine.count('r')
u=combine.count('u')
e=combine.count('e')
l=combine.count('l')
o=combine.count('o')
v=combine.count('v')
e=combine.count('e')

true=t+r+u+e
love=l+o+v+e


truelove=int(str(true)+str(love))
print(truelove)

if truelove<10:
  print("your score:",truelove)
elif truelove>=10 and truelove<=50:
  print("good couple , your score is",truelove )
elif truelove>=50 and truelove<=100:
  print("great couple , your score is",truelove )







