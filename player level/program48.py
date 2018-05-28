def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
g=int(input())
f=[]
o=[]
if(g!=1):
  for i in range(2,g+1):
    k=0
    while g%i==0:
      g=g/i
      if k==0 and i%2==1:
        f.append(i)
        k=k+1
  display(f)
else:
  print('1')
    
