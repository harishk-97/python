kira=int(input())
hero=input().split()
hero=list(map(int,hero))
tester=[]
for i in range(kira):
  tester.append(1)
loudo=sorted(hero)
shiko=[]
candy=1
for i in loudo:
  if i not in shiko:
    shiko.append(i)
listy=hero
if(kira>1):
  for value in shiko:
    position=[]
    n=0
    for i in range(len(listy)):
      if(value==listy[i]):
        n+=1
    tera=listy
    for i in range(len(tera)):
      if(tera[i]==value):
        position.append(i)
    for i in position:
      if(i==0):
        if(hero[i]>hero[i+1]):
          tester[i]=tester[i+1]+1
        elif(hero[i]==hero[i+1]):
          tester[i]=tester[i+1]
      elif(i==kira-1):
        if(hero[i]>hero[i-1]):
          tester[i]=tester[i-1]+1
        elif(hero[i]==hero[i-1]):
          tester[i]=tester[i-1]
      else:
        if(hero[i]>hero[i+1] and hero[i]>hero[i-1]):
          if(hero[i+1]>hero[i-1]):
            tester[i]=tester[i+1]+1
          elif(hero[i+1]<hero[i-1]):
            tester[i]=tester[i-1]+1
        elif(hero[i]>hero[i+1] and hero[i]<hero[i-1]):
          tester[i]=tester[i+1]+1
        elif(hero[i]<hero[i+1] and hero[i]>hero[i-1]):
          tester[i]=tester[i-1]+1
        elif(hero[i]>hero[i+1] and hero[i]==hero[i-1]):
          tester[i]=tester[i+1]+1 
          if(tester[i]<tester[i-1]):
            tester[i]=tester[i-1]
        elif(hero[i]>hero[i-1] and hero[i]==hero[i+1]):
          tester[i]=tester[i-1]+1 
          if(tester[i]<tester[i+1]):
            tester[i]=tester[i+1]
        elif(hero[i]==hero[i+1] and hero[i]==hero[i-1]):
          tester[i]=tester[i-1]
          if(tester[i+1]>tester[i-1]):
            tester[i]=tester[i+1]
          else:
            tester[i]=tester[i-1]
  for i in range(kira-1,0,-1):
    if(i!=kira-1 and i!=0):
      if(hero[i]==hero[i+1]):
        tester[i]=tester[i+1]
print(sum(tester))
          
