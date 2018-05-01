n=int(input())
q=0
if(abs(n)==n):
  for i in range(2,n):
   if(n%i==0):
     q=1
if(q==1):
  print('yes')
else:
  print('no')
