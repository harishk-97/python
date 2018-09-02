n=input().split()
m=0
for i in range(len(n[0])-1):
  for j in range(len(n[1])-1):
    if((n[0][i]+n[0][i+1])==(n[1][j]+n[1][j+1])):
      m=1
if(m==1):
  print('yes')
else:
  print('no')
