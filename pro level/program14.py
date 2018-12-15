a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=[]
for i in range(a[1]):
  c=list(map(int,input().split()))
  d=b[(c[0]-1)]^b[(c[0])]
  for j in range(c[0]+1,c[1]):
    d=d^b[j]
  e.append(d)
for i in range(len(e)):
  print(e[i])
