n=input()
m=len(n)
q=int(m/2)
if(m%2!=0):
  for i in range (m):
    if(i!=q):
      print(n[i],end='')
    else:
      print('*',end='')
else:
  for i in range (m):
    if(i!=q and i!=(q-1)):
      print(n[i],end='')
    else:
      print('*',end='')  
