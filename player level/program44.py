s=input().split()
t=int(s[1])
u=len(s[0])
v=t%u
c=''
o=''
for i in range(u-v,u):
  c+=s[0][i]
for i in range(u-v):
  o+=s[0][i]
print(c,o,sep='')
