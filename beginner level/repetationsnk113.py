g=input().split()
g=list(map(int,g))
b=input().split()
b=list(map(int,b))
n=0
for i in range(len(b)):
  if(g[1]==b[i]):
    n=n+1
print(n)
