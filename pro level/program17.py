def sumpair(a,b,c):
  for i in range(a):
    for j in range(i+1,a):
      if((c[i]+c[j])==b):
        return('yes')
  return('no')
d=input().split()
d=list(map(int,d))
e=input().split()
e=list(map(int,e))
print(sumpair(d[0],d[1],e))
