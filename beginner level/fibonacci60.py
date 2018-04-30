y=int(input())
k=[1,1]
m=[]
if(y>1):
  for i in range(y-1):
    m.append(k[0])
    m.append(k[1])
    k[0]=k[0]+k[1]
    k[1]=k[0]+k[1]
  for i in range(y):
    if(i==0):
      print(m[i],end='')
    else:
      print('',m[i],end='')
elif(y==1):
  print('1')
