n=input()
m=len(n)
q=[]
for i in range(m):
  a=n[i]
  p=1
  for j in range(m):
    if(j!=i):
      if(n[i]==n[j]):
        p=p+1
  q.append(p)
q=list(map(int,q))
if(max(q)==min(q)):
  print('Yes')
else:
  print('No')
        
    
  
  
