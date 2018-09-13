z=input().split()
z=list(map(int,z))
if(z[1]!=z[0]):
  print('1',end=' ')
if((z[0]-z[1])<(2*z[1])):
  print(z[0]-z[1])
else:
  if(z[1]==0):
    print("0",end=' ')
    print('0')
  else:
    print(2*z[1])
