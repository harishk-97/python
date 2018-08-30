a=int(input())
k=input().split()
k=list(map(int,k))
b=[]
c=[]
for i in range(a):
  b.append(k[i])
  c.append(min(b))
for i in range(len(c)):
  if(i==0):
    print(c[i],end='') 
  else:
    print("",c[i],end='') 
  
