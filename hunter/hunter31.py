w=int(input())
x=input().split()
x=list(map(int,x))
m=1
for i in x:
  if i>0:
    m*=i
print(m)
