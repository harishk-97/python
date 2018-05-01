a=input()
l=len(a)
b=[]
for i in range(l):
  c=ord(a[i])
  b.append(c)
b=sorted(b)
for i in range(l):
  print(chr(b[i]),end='')
