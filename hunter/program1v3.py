f=int(input())
g=input().split()
g=list(map(int,g))
h=[]
for i in range(len(g)):
  for j in range(len(g)):
    if(i!=j):
      if(g[i]==g[j]):
        if g[i] not in h:
          h.append(g[i])
h=sorted(h)
for i in range(len(h)):
  if(i!=(len(h)-1)):
    print(h[i],end=' ')
  else:
    print(h[i])
if(h==[]):
  print('unique')
  
        
  
