z=input().split()
y=len(z[0])
x=int(z[1])
w=y-x
e=z[0]
g=[]
for i in range(x+1):
  f=''
  d=[]
  for j in range(i,w+i):
    d.append(e[j])
  for k in range(0,y-x):
    f+=d[k]
  g.append(f)
g=list(map(int,g))
v=str(min(g))
u=len(v)
def nulladd(zer,ker):
  for i in range(ker):
    zer='0'+zer
  print(zer)
if(w==u):
  print(v)
else:
  nulladd(v,w-u)
