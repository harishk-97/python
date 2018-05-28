def gcd(list):
    m=1
    for i in range(1,max(list)+1):
        n=0
        for j in range(len(list)):
            if(list[j]%i==0):
                n+=1
        if(n==len(list)):
            m=i
    print(m)
b=input().split()
b=list(map(int,b))
l=input().split()
l=list(map(int,l))
lod=[]
for i in range(b[1]):
    c=input().split()
    c=list(map(int,c))
    lod.append(c)
for i in range(len(lod)):
    new=[]
    for j in range((lod[i][0]-1),(lod[i][1])):
        new.append(l[j])
    gcd(new)
        
