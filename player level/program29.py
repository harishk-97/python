a=input().split()
a=list(map(int,a))
b=max(a)
s=0
for i in range(1,b+1):
  c=i**2
  if(c>=a[0] and c<=a[1]):
    s=s+1
print(s)
