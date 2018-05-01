g=input().split()
a=int(g[1])
b=str(g[0])
c=len(b)
for i in range(c-a,c):
  print(b[i],end='')
