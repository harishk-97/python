s=input().split()
s=list(map(int,s))
p=int(s[0]/2)
q=0
for i in range(1,p):
  for j in range(1,p):
    if((i*j==s[1]) and (i+j==p)):
      q=1
if(q==1):
  print('yes')
else:
  print('no')
