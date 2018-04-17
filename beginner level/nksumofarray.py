give=int(input())
k=int(input())
l=[]
n=0
for i in range(give):
  m=int(input())
  l.append(m)
for i in range(k):
  n=l[i]+n
print(n)
