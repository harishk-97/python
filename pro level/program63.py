def stylo(m):
  x=0
  for i in range(len(m)):
    for j in range(i+1,len(m)):
      if(m[i]==m[j]):
        return 0
  return(len(m))
w=input()
x=[]
for i in range(len(w)):
  for j in range(i+1,len(w)+1):
    x.append(stylo(w[i:j]))
print(max(x))
