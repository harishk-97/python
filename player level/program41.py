d=input().split()
d=list(map(int,d))
m=d[1]
k=0
for i in range(100):
  c=m**i
  if(c==d[0]):
    k=1
    break
if(k==1):
  print('yes')
else:
  print('no')
