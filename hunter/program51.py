def product(los):
    m=1
    for i in range(len(los)):
        m*=los[i]
    return(m)
a=input().split()
a=list(map(int,a))
print(product(a))
