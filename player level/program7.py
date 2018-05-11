a=input().split()
a1=len(a)
for i in range(a1):
  b=a[i]
  for j in range(len(b)):
    if(j==0):
      print(b[j].upper(),end='')
    else:
      print(b[j],end='')
  if(i!=a1-1):
    print(' ',end='')
 
