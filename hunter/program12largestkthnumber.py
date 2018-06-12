g=input().split()
g=list(map(int,g))
h=input().split()
h=list(map(int,h))
for i in range(1,g[1]):
  h.remove(max(h))
print(max(h))
