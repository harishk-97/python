rk=input()
c=0
for i in range(len(rk)):
  for j in range(len(rk)):
    if(i!=j):
      if(rk[i]==rk[j]):
        c=1
if(c==1):
  print('yes')
else:
  print('no')

