def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
g=int(input())
m=input().split()
m=list(map(int,m))
f=[]
for i in m:
  if(g>i):
    f.append(i)
display(sorted(f))
