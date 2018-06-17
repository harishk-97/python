g=input()
import itertools
h=len(g)
l=[]
for i in range(h):
  l.append(g[i])
s=list(itertools.permutations(l))
m=[]
for i in s:
  if i not in m:
    m.append(i)
for i in range(len(m)):
  n=len(m[i])
  for j in range(n):
    print(m[i][j],end='') 
  print("")
