g=input().split()
c=0
for i in range(len(g[1])):
  for j in range(len(g[0])):
    if(g[1][i]==g[0][j]):
      c=1
if(c==1):
  print('yes')
else:
  print('no')
  
