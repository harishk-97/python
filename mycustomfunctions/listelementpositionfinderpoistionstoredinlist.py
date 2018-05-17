def listpositonfind(list,value,position):
  position=[]
  n=0
  for i in range(len(list)):
    if(value==list[i]):
      n+=1
  kira=list
  for i in range(len(kira)):
    if(kira[i]==value):
      position.append(i)
  
the below code id to remove duplicates in the list:

def listtoberemovedduplictes(listname,uniquelist):
  for i in listname:
    if i not in uniquelist:
      uniquelist.append(i)
