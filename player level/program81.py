a=int(input())
b=input().split()
b=list(map(int,b))
n=0
for i in range(a):
    if(n<b[i]):
        n=b[i]
print(n)
