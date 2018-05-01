n=int(input())
m=input().split()
m=list(map(int,m))
q=0
a=m[0]+1
b=m[1]
for i in range(a,b):
  if(a==n):
    q=1
if(q==1):
  print("yes")
else:
  print("no")
