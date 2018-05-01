n=input().split()
n=list(map(int,n))
for i in range(1,(min(n)+1)):
  if(n[0]%i==0 and n[1]%i==0):
    a=i
print(a)
