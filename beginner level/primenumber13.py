a=int(input())
n=0
for i in range(a):
  if(i>1):
    if(a%i==0):
      n=1
if(n==0):
  print('yes')
else:
  print('no')
