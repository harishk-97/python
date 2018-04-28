z=input().split()
z=list(map(int,z))
z[0]=z[0]+1
while(z[0]<z[1]):
  n=0
  for i in range(z[0]):
    if(i>1):
      if(z[0]%i==0):
        n=1 
  if(n==0):
    print(z[0],end=' ')
  z[0]=z[0]+1
