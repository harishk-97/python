n=int(input())
m=input().split()
m=list(map(int,m))
a=sorted(m)
b=len(m)
c=0
while(c<b):
  if(m[c]!=a[c]):
    print(m[c])
    c=b
  c=c+1

  
