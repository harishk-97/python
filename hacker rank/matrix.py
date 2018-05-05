a=int(input())
b=[]
for i in range(a):
  c=input().split()
  c=list(map(int,c))
  b.append(c)
d=0
e=0
for i in range(a):
  for j in range(a):
    if(i==j):
      d+=b[i][j]
b=b[::-1]
for i in range(a):
  for j in range(a):
    if(i==j):
      e+=b[i][j]
print(abs(d-e))
    
    
