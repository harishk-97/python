z=input().split()
z=list(map(int,z))
a=z[0]
z[0]=z[1]
z[1]=a
print(z[0],z[1])
