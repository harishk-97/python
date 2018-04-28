i=input().split()
i=list(map(int,i))
if(i[0]%2==0):
  g=i[0]+1
  while(g<i[1]):
    if(i[1]%2==0):
      if(i[1]==g+1):
        print(g,end='')
      else:
        print(g,end=' ')
    else:
      if(i[1]==g+2):
        print(g,end='')
      else:
        print(g,end=' ')
    g=g+2
elif(i[0]%2!=0):
  g=i[0]+2
  while(g<i[1]):
    if(i[1]%2==0):
      if(i[1]==g+1):
        print(g,end='')
      else:
          print(g,end=' ')
    else:
      if(i[1]==g+2):
        print(g,end='')
      else:
        print(g,end=' ')
    g=g+2
