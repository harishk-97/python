a=input()
if(len(a)%2==0):
  for i in range(0,len(a),2):
    print(a[i+1],a[i],sep='',end='')
else:
  for i in range(0,len(a),2):
    if(i!=len(a)-1):
      print(a[i+1],a[i],sep='',end='')
    else:
      print(a[i])
  
