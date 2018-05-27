d=int(input())
e=[]
for i in range(1,d+1):
  if(d%i==0 and i%2==0):
    e.append(i)
def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
display(e)
