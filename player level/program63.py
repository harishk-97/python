def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
l=int(input())
g=input().split()
g=list(map(int,g))
h=input().split()
h=list(map(int,h))
f=[]
for i in g:
  if i in h:
    if i not in f:
      f.append(i)
display(f)

