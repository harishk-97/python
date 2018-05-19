kun=int(input())
sun=input().split()
sun=list(map(int,sun))
m=0
for n in range(kun):
  if(n%2==0 and sun[n]%2==1):
    if(m==0):
      print(sun[n],end='')
      m=1
    else:
      print('',sun[n],end='')
  if(n%2==1 and sun[n]%2==0):
    if(m==0):
      print(sun[n],end='')
      m=1
    else:
      print('',sun[n],end='')
