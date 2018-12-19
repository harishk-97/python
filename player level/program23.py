a=list(map(int,input().split()))
m=input()
b=list(map(int,input().split()))
c=list(map(int,input().split()))
flag=0
for i in range(a[1]):
  b.append(c[i])
  if(flag==0):
    print(max(b),end='')
    flag+=1
  else:
    print('',max(b),end='')

