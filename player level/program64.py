def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
g=input().split()
g=list(map(int,g))
m=input().split()
m=list(map(int,m))
f=[]
for i in m:
  if(g[1]>i):
    f.append(i)
display(sorted(f))
