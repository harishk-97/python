n=int(input())
k=input().split()
k=list(map(int,k))
m=sorted(k)
k=0
for i in range (n):
  if(k==0):
    print(m[i],end='')
    k=k+1
  else:
    print("",m[i],end='')
