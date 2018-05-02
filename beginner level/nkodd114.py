z=input().split()
z=list(map(int,z))
a=input().split()
a=list(map(int,a))
b=z[1]
c=0
for i in range(len(a)):
  if(a[i]%2==1):
    c=c+1
    if(c==b):
      print(a[i])
  
  
