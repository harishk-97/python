z=int(input())
y=z
w=z
n=1
m=0
while z>=10:
  n=n+1
  z=z/10
if (n==1 & y!=0):
  print('yes')
elif(n==1 & y==0):
  print('no')
elif(n==2):
  print('no')
elif(n>2):
  while(y!=0):
    x=y%10
    x=x**n
    m=m+x
    y=int(y/10)
  if(m==w):
    print('yes')
  else:
    print('no')
