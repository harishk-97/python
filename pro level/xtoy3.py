z=input().split()
y=z[0]
x=z[1]
w=[]
v=[]
for k in range(len(y)):
  w.append(ord(y[k]))
for k in range(len(x)):
  v.append(ord(x[k]))
if((len(w))==(len(v))):
  u=0
  for i in range(len(w)):
    if(w[i]!=v[i]):
      u=u+1
elif(len(w)>len(v)):
  u=0
  t=len(w)-len(v)
  for i in range(len(v)):
    if(w[i]!=v[i]):
      u=u+1
  u=u+t
else:
  u=0
  t=len(v)-len(w)
  for i in range(len(w)):
    if(w[i]!=v[i]):
      u=u+1
  u=u+t
print(u)
