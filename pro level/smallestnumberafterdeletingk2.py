a=input().split()
b=len(a[0])
c=int(a[1])
h=b-c
e=a[0]
g=[]
for i in range(c+1):
  f=''
  d=[]
  for j in range(i,h+i):
    d.append(e[j])
  for k in range(0,b-c):
    f+=d[k]
  g.append(f)
g=list(map(int,g))
print(min(g))
