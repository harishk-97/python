a=int(input())
b=input().split()
b=list(map(int,b))
c=[]
j=1
for i in range(a):
  if(i==b[i]):
    if j==1:
      print(i,end='')
      j=0
    else:
      print('',i,end='')
      
      
  
