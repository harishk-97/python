a=input().split()
a=list(map(int,a))
b=input().split()
b=list(map(int,b))
c=int(input())
m=0
for i in range(a[0]):
  if(i!=a[1]):
    m+=b[i]
if((m/2)==c):
  print('Bon Appetit')
else:
  print(c-int(m/2))
