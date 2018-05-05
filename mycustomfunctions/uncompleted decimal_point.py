def decimal_point(number,nodp):
  a=int(number)
  d=len(str(a))
  b=str(number)
  c=len(b)
  f=c-d+1
  g=nodp+d+1
  h=''
  if(nodp<f):
    for i in range(g):
      h+=b[i]
  elif(nodp>f):
    for i in range(g):
      if(i<c):
        h+=b[i]
      else:
        h+='0'
      print(h)
  else:
    h=b
  print(h)
decimal_point(23.235078,8)
      
  
