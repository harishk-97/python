a=input().split()
b=len(a[0])
c=len(a[1])
a1=a[0]
a2=a[1]
d1=0
d2=0
for i in range(b-1):
  if(a1[i]!=a1[i+1]):
    d1=d1+1
for i in range(c-1):
  if(a2[i]!=a2[i+1]):
    d2=d2+1
if(d1==d2):
  print('yes')
else:
  print('no')
