k=input().split()
k=list(map(int,k))
k[0]=k[0]+1
p=0
while(k[0]<k[1]):
  y=k[0]
  w=k[0]
  n=1
  m=0
  while w>=10:
    n=n+1
    w=w/10
  while y!=0:
    x=y%10
    x=x**n
    m=m+x
    y=int(y/10)
  if m==k[0]:
    if(p==0):
      print(m,end='')
      p=1
    else:
      print("",m,end='')
  k[0]=k[0]+1

  
