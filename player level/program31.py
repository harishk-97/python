a=input()
m=0
n=0
for i in range(len(a)):
  if(a[i]=='('):
    m+=1
  else:
    n+=1
if(m==n):
  print('yes')
else:
  print('no')
