m=int(input())
q=0
if(abs(m)==m):
  for i in range(2,m):
   if(m%i==0):
     q=1
if(q==1):
  print('yes')
else:
  print('no')
