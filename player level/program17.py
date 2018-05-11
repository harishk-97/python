f=input().split()
f=list(map(int,f))
i=0
g=max(f)
while(i==0):
  if(g%f[0]==0 and g%f[1]==0):
    i=1
    print(g)
  g+=1
