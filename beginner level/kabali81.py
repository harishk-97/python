n=input().split()
n=list(map(int,n))
if(n[0]<4294967296 and n[1]<4294967296):
  print(abs(n[0]-n[1]))
else:
  print('End of File')
