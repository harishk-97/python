a=int(input())
b=input().split()
b=list(map(int,b))
c=b[0]
m=0
for i in range(a):
    if(c!=b[i]):
        m=1
if(m==1):
    print("0")
else:
    print(c)
