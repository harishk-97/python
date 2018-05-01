n=int(input())
for i in range(1,(n+1)):
  if(i==1 and n%i==0):
    print(i,end='')
  elif(i!=1 and n%i==0):
    print("",i,end='')
  
