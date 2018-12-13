def repeat(a,b,c):
  d=[]
  for i in range(b):
    flag=0
    for j in range(1,a):
      if c[0][i] in c[j]:
        flag+=1
    if((flag+1)==a and c[0][i] not in d):
      d.append(c[0][i])
  d=sorted(d)
  for i in range(len(d)):
    if i==0:
      print(d[i],end='')
    else:
      print('',d[i],end='')    

a=input().split()
a=list(map(int,a))
b=[]
for i in range(a[0]):
  b.append(list(map(int,input().split())))
repeat(a[0],a[1],b)
