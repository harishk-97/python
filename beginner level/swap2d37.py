m=input().split()
m=list(map(int,m))
a=m[0]
m[0]=m[1]
m[1]=a
print(m[0],m[1])
