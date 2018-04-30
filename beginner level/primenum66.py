y=int(input())
m=1
for i in range(2,y):
  if(y%i==0):
    m=0
if(m==1):
  print('yes')
else:
  print('no')
