m=input().split()
if(len(m[0])==len(m[1])):
  c=0
  for i in range(len(m[0])):
    if(m[0][i]==m[1][i]):
      c+=1
  if(c==len(m[0])):
    print('yes')
  else:
    print('no')
else:
  print('no')
