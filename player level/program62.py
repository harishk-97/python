g=int(input())
for i in range(1,g+1):
  if(g%i==0):
    ch=g/i
  if(ch%2==1):
    ans=i
    break
print(ans)
