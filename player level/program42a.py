m=int(input())
d=input().split()
d=list(map(int,d))
if(m<2):
  print('yes')
else:
  k=0
  for i in range(m-1):
    if(d[i]+1==(d[i+1])):
      k+=1
  if(k==(m-1)):
    print('yes')
  else:
    print('no')
    
