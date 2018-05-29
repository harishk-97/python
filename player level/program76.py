h=int(input())
mr=input().split()
mr=list(map(int,mr))
e=0
o=0
for i in mr:
  if(i%2==0):
    e+=1
  else:
    o+=1
if(e>o):
  for i in mr:
    if(i%2!=0):
      print(i)
else:
  for i in mr:
    if(i%2==0):
      print(i)
