a=input().split()
k=int(a[2])
c=0
m=a[0]
n=a[1]
q=min(len(m),len(n))
r=max(len(m),len(n))
for i in range(q):
  if(m[i]==n[i]):
    c=c
  else:
    c+=1
s=r-q
c=c+s
if(k==c):
  print('yes')
else:
  print('no')
