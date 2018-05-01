j=int(input())
l=[]
while(j>0):
  r=j%10
  if(r%2!=0):
    l.append(r)
  j=int(j/10)
l=l[::-1]
a=len(l)
for i in range(a):
  if(i==0):
    print(l[i],end='')
  else:
    print("",l[i],end='')
