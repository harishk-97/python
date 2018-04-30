z=int(input())
k=[1,1]
m=[]
if(z>1):
  for i in range(z-1):
    m.append(k[0])
    m.append(k[1])
    k[0]=k[0]+k[1]
    k[1]=k[0]+k[1]
  for i in range(z):
    if(i==0):
      print(m[i],end='')
    else:
      print('',m[i],end='')
elif(z==1):
  print('1')
  
