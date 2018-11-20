a=input().split()
a=list(map(int,a))
b=input().split()
b=list(map(int,b))
c=[]
for i in range(a[1]):
  d=input().split()
  c.append(list(map(int,d)))
for i in range(a[1]):
  print(min(b[(c[i][0]-1):c[i][1]]))

