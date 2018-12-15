a=list(map(int,input().split()))
b=sorted(list(map(int,input().split())))[::-1]
n=0
for i in range(len(b)):
  if(a[1]>=b[i]):
    n+=int(a[1]/b[i])
    a[1]%=b[i]
if(a[1]==0):
  print(n)
else:
  print("it's not possible to select coins in such a way that they sum upto S")
