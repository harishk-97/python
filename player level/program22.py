garou=input().split()
garou=list(map(int,garou))
m=min(garou)
a=0
for i in range(1,m+1):
  if(garou[0]%i==0 and garou[1]%i==0):
    a=i
print(a)
