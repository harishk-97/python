def looper(n):
  i=0
  while(i<(n+int(n/2))):
    q=2
    while(q<=n):
      if(i+1==(n+int(n/2))):
        print(q)
        return
      else:
        print(q,end=' ')
        q+=2
        i+=1
    q=1
    while(q<=n):
      if(i+1==(n+int(n/2))):
        print(q)
        return
      else:
        print(q,end=' ')
        q+=2
        i+=1    
n=int(input())
print(n+int(n/2))
looper(n)
