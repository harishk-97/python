m=input().split()
m=list(map(int,m))
n=input().split()
n=list(map(int,n))
for i in range(m[1]-1):
  n.remove(min(n))
print(min(n))
