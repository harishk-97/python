a=input().split()
a=list(map(int,a))
b=max(a)
c=min(a)
d=[]
for i in range(b,1,-1):
  if(b%i==0 and c%i==0):
    d.append(i)
    b=int(b/i)
    c=int(c/i)
d.append(b)
d.append(c)
e=1
for f in d:
  e*=f
print(e)
