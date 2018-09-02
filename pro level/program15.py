y=int(input())
z=list(map(int,input().split()))
for i in range(len(z)):
  print(max(z))
  z.remove(max(z))
