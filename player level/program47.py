a=input().split()
a=list(map(int,a))
if 0 not in a:
  if(sum(a)==180):
    print('yes')
  else:
    print('no')
else:
  print('no')
  
