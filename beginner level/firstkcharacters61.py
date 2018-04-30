y=input().split()
a=int(y[1])
b=y[0]
for i in range(a):
  if(i==a-1):
    print(b[i])
  else:
    print(b[i],end='')
