s=int(input())
q=input().split()
q=list(map(int,q))
for i in range(len(q)):
  x=1
  for j in range(i+1,len(q)):
    if((q[j]>0 and q[j-1]<0)or(q[j]<0 and q[j-1]>0)):
      x+=1
    else:
      break
  if(i!=(len(q)-1)):
    print(x,end=' ')
  else:
    print(x,end='')
