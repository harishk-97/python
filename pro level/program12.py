hero=input().split()
hero=list(map(int,hero))
kira=input().split()
kira=list(map(int,kira))
dre=[]
for i in range(hero[1]):
  mrl=input().split()
  mrl=list(map(int,mrl))
  dre.append(mrl)
for i in range(len(dre)):
  zero=0
  for j in range((dre[i][0]-1),(dre[i][1])):
    zero+=kira[j]
  print(zero)
