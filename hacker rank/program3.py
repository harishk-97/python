a=int(input())
p=a
for i in range(a):
  b=''
  for i in range(a):
    if(i<p-1):
      b+=' '
    else:
      b+='#'
  p=p-1
  print(b)
 
    
  
