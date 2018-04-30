y=input().split()
x=len(y)
p=0
q=0
for i in range(x):
  a=y[i]
  b=len(y[i])
  for j in range(b):
    if(a[j].isdigit()):
      p=1
    else:
      q=1
if(p==1 and q==1):
  print('Yes')
else:
  print('No')
