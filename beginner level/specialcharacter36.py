z=input().split()
n=0
m=0
for i in range(len(z)):
  a=z[i]
  m=m+len(a)
  for i in range(len(a)):
    if(a[i].isdigit()):
      n=n+1
    elif(a[i].isalpha()):
      n=n+1
    elif(a[i]=='.'):
      n=n+1
print(m-n)
  
