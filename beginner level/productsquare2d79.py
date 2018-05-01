j=input().split()
j=list(map(int,j))
a=j[0]
b=j[1]
c=a*b
d=0
if(c!=1):
  for i in range(1,c):
    if((i*i)==c):
     d=1
  if(d==1):
    print('yes')
  else:
    print('no')
else:
  print('yes')
