a=input()
a=sorted(a)
b=[]
for i in range(len(a)):
  if a[i] not in b:
    b.append(a[i])
d=[]
for i in range(len(b)):
  c=0
  for j in range(len(a)):
    if(b[i]==a[j]):
      c+=1
  d.append(c)
e=d.index(max(d))
print(b[e])
  
  
