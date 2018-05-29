h=int(input())
mr=input().split()
mr=list(map(int,mr))
c=0
for i in range(h):
  for j in range(i,h):
    if(mr[i]<mr[j]):
      c+=1
print(c)
