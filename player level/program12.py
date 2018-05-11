a=input().split()
a=list(map(int,a))
b=input().split()
for i in range(a[1]):
  c=b.pop()
  b=b[::-1]
  b.append(c)
  b=b[::-1]
for i in range(a[0]):
  if(i==0):
    print(b[i],end='')
  else:
    print('',b[i],end='')

  
