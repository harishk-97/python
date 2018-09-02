n=int(input())
while(n%10==0):
  n/=10
n=str(int(n))
if(n==n[::-1]):
  print('yes')
else:
  print('no')
