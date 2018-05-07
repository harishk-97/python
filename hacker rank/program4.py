a=input().split()
a=list(map(int,a))
b=[]
for i in range(5):
  c=0
  for j in range(5):
    if(i==j):
      c+=0
    else:
      c+=a[j]
  b.append(c)
print(min(b),max(b),sep=' ')


      
    
  
