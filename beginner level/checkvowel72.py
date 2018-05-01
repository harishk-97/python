n=input()
m=len(n)
q=0
for i in range(m):
  a=ord(n[i])
  if(a==65 or a==69 or a==73 or a==79 or a==85):
    q=1
  elif(a==97 or a==101 or a==105 or a==111 or a==117):
    q=1
if(q==1):
  print('yes')
else:
  print('no')
