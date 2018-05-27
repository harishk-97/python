m=int(input())
d=input().split()
d=list(map(int,d))
if(d==sorted(d)):
  print('yes')
else:
  print('no')
