g=input().split()
g=list(map(int,g))
h=input().split()
h=list(map(int,h))
j=input().split()
j=list(map(int,j))
n=0
for i in j:
  if i in h:
    n+=1
    h.remove(i)
if(n==g[1]):
  print('YES')
else:
  print('NO') 
