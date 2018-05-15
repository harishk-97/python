x=input()
y=input()
x1=[]
y1=[]
z=[]
for i in range(len(x)):
  x1.append((ord(x[i]))%96)
  y1.append((ord(y[i]))%96)
  z.append(x1[i]+y1[i])
for j in z:
  if(j<=26):
    print(chr(j+96),end='')
  else:
    j=j%26
    if(j==0):
      j=26
    print(chr(j+96),end='')
