z=int(input())
y=[]
t=[]
for i in range(z):
  x=input()
  y.append(x)
w=y[0]
def compare(r,s):
  u=0
  v=0
  for j in range(min(len(r),len(s))):
    if(r[j]==s[j] and v==0):
      u=u+1
    else:
      v=1
  t.append(u)
for i in range(1,z):
  compare(y[0],y[i])
for k in range(min(t)):
  print(w[k],end='',sep='')
