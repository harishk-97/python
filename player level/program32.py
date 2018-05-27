a=input().split()
a=list(map(int,a))
m=input().split()
m=list(map(int,m))
if a[1] in m:
  print('Yes')
else:
  print('No')
