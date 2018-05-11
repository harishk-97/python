a=int(input())
b=input().split()
b=list(map(int,b))
b=sorted(b)
c=0
i=0
while(i<a):
  if(i!=a-1):
    if(b[i]!=b[i+1]):
      d=b[i]
      c=1
  elif(c==0 and i==a-1):
    d=b[i]
    c=1
  i=i+2
  if(c==1):
    i=a
print(d)
    
    
