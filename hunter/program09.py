a=int(input())
b=input().split()
b=list(map(int,b))
c=[]
for i in range(a):
  for j in range(a):
    if(i!=j and j>i):
      d=[b[i],b[j],abs(b[i]+b[j])]
      c.append(d)
e=c[0][2]
for i in range(1,len(c)):
  if(e>c[i][2]):
    e=c[i][2]
for i in range(len(c)):
  if(e==c[i][2]):
    print(c[i][0],c[i][1],sep=' ')
    break

  
