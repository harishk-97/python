gun=int(input())
sun=input().split()
sun=list(map(int,sun))
m=0
for i in range(gun):
  if(i%2==0 and sun[i]%2==1):
    if(m==0):
      print(sun[i],end='')
      m=1
    else:
      print('',sun[i],end='')
  if(i%2==1 and sun[i]%2==0):
    if(m==0):
      print(sun[i],end='')
      m=1
    else:
      print('',sun[i],end='')


    
