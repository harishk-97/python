def display(q):
  for i in range(len(q)):
    if(i==0):
      print(q[i],end='')
    else:
      print("",q[i],end='')
l=input().split()
l=list(map(int,l))
g=input().split()
g=list(map(int,g))
q=[]
for i in g:
  n=0
  for j in g:
    if(i==j):
      n+=1
  if(n==l[1]):
    if i not in q:
      q.append(i)
display(q)
