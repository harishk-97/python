g=input().split()
for i in range(len(g)):
  b=g[i]
  print(b[::-1],end='')
  if(i!=(len(g)-1)):
    print(" ",end='')
