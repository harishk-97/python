g=input().split()
g=list(map(int,g))
h=input().split()
h=list(map(int,h))
if g[1] not in h:
  h.append(g[1])
h=sorted(h)
m=h.index(g[1])
n=len(h)
if(m==0):
  print(h[1],h[2],h[3],sep=' ')
elif(m==1):
  print(h[0],h[2],h[3],sep=' ')
elif(m==n-1):
  print(h[n-2],h[n-3],h[n-4],sep=' ')
else:
  print(h[m-1],h[m+1],h[m-2],sep=' ')
