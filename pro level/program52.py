s=[]
m,n=0,0
for i in range(4):
  s.append(list(map(int,input().split())))
  m+=s[i][0]
  n+=s[i][1]
if(m==n):
  print('yes')
else:
  print('no')
