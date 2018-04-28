z=input().split()
z=list(map(int,z))
if(z[0]%2==0):
  g=z[0]+2
  while(g<z[1]):
    print(g,end=' ')
    g=g+2
elif(z[0]%2!=0):
  g=z[0]+1
  while(g<z[1]):
    print(g,end=' ')
    g=g+2
