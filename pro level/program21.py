a=int(input())
b=input().split()
b=list(map(int,b))
m=0
for i in range(1,a):
  n=0
  p=0
  for j in range(i):
    n+=b[j]
  n=int(n/i);
  for k in range(i,a):
    p+=b[k]
  k=a-i
  p=int(p/k)
  if(n==p):
    m=1
if(m==1):
  print("yes")
else:
  print("no")
