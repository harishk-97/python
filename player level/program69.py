def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
mi=input().split()
mi=list(map(int,mi))
gt=input().split()
gt=list(map(int,gt))
for i in range(mi[1]):
  gt.pop()
display(gt)
