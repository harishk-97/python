a=input().split()
for i in range(len(a)):
  b=a[i]
  if(i!=0):
    print(" ",end='')
  for j in range(len(b)):
    if(j==0):
      print(b[j].upper(),end='')
    else:
      print(b[j],end='')
