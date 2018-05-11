a=int(input())
b=input().split()
b=list(map(int,b))
c=[]
j=1
for i in range(a):
  if(i==b[i]):
    c.append(i)
c=sorted(c)
for i in range(len(c)):
  if j==1:
    print(c[i],end='')
    j=0
  else:
    print('',c[i],end='')
if(len(c)==0):
  print('-1')
 
