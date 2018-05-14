n=int(input())
r=0
q=[97, 97, 98, 105, 107, 108]
for i in range(n):
  p=[]
  m=input()
  for j in range(len(m)):
    p.append(ord(m[j]))
  if(q==sorted(p)):
    r+=1
print(r)
