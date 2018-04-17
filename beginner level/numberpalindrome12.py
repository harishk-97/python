a=int(input())
m=[]
while a>0:
  c=a%10
  m.append(c)
  a=int(a/10)
j=m[::-1]
if(m==j):
  print('yes')
else:
  print('no')
