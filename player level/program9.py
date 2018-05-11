a=input().split()
a=list(map(int,a))
l=0
for i in range(a[0],a[1]+1):
  k=0
  for j in range(2,i):
    if(i%j==0):
      k=1
  if(k==0):
    l+=1
print(l)
