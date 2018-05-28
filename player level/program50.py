m=int(input())
n=0
for i in range(2,m):
  if(m%i==0):
    n=1
if(n==1):
  print('yes')
else:
  print('no')
