x=int(input())
y=input().split()
y=sorted(y)
a=0
z=[]
for i in y:
  if(len(i)>a):
    a=len(i)
for i in range(a+1):
  for j in y:
    if(i==len(j)):
      z.append(j)
def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
display(z)
