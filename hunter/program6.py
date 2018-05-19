gun=int(input())
sun=input().split()
sun=list(map(int,sun))
n=[]
m=None
for i in sun:
  if i not in n:
    n.append(i)
  else:
    m=i
    break
if m is not None:
  print(m)  
else:
  print('unique')
