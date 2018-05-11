a=int(input())
b=input().split()
b=list(map(int,b))
b=sorted(b)[::-1]
b=list(map(str,b))
c=''
for i in range(a):
  c+=b[i]
print(int(c))
    
  
