a=input().split()
a=list(map(int,a))
b=input().split()
b=list(map(int,b))
c=input().split()
c=list(map(int,c))
n=0
for i in c:
  if i in b:
    n+=1
if(n==a[1]):
  print('YES')
else:
  print('NO')
