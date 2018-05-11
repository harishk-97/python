a=input().split()
b=len(min(a))
a=list(map(list,a))
c=0
for i in range(b):
  if(a[1][i]!=a[0][i]):
    c+=1
if(c==1):
  print('yes')
else:
  print('no')
