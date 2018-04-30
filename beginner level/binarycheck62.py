y=input()
x=len(y)
m=0
for i in range(x):
  a=int(y[i])
  if(a==0 or a==1):
    m=m+1
if(m==x):
  print('yes')
else:
  print('no')
