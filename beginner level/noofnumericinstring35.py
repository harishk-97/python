m=input()
n=len(m)
p=0
for i in range(n):
  if(m[i].isdigit()):
    p=p+1
print(p)
