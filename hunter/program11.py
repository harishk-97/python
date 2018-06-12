g=input().split()
for i in range(len(g)):
  b=g[i]
  for j in range((len(b)-1),-1,-1):
    print(b[j],end='')
  if(i!=(len(g)-1)):
    print(" ",end='')
