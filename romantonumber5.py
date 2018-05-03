g=input()
a=0
for i in range(len(g)):
  if(i==0):
    if(g[i]=='I'):
      a=a+1
    elif(g[i]=='V'):
      a=a+5
    elif(g[i]=='X'):
      a=a+10
  if(i==1):
    if(g[i]=='I'):
      a=a+1
    elif(g[i]=='V' and a==1):
      a=a+3
    elif(g[i]=='V' and a>1):
      a=a+5
    elif(a==1 and g[i]=='X'):
      a=a+8
    elif(a==10 and g[i]=='X'):
      a=a+10
  if(i==2):
    if(g[i]=='I'):
      a=a+1
    elif(g[i]=='V'):
      a=a+3
    elif(g[i]=='X'):
      a=a+8
  if(i==3):
    if(g[i]=='I'):
      a=a+1
  if(i==4):
    if(g[i]=='I'):
      a=a+1
print(a)
    
