g=int(input())
q=[]
for i in range(2,g+1):
  if(g%i==0):
    q.append(i)
    while(g%i==0):
      g=g/i
def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
display(q)
      
      
