g=input().split()
g=list(map(int,g))
b=input().split()
b=list(map(int,b))
if g[1] in b:
  print('yes')
else:
  print('no')
