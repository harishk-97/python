def decimal_point(number,nodp):
  a=int(number)
  d=len(str(a))
  b=str(number)
  c=len(b)
  f=c-d-1
  g=nodp+d+1
  h=''
  if(nodp<f):
    for i in range(g):
      if(i!=g-1):
        h+=b[i]
      else:
        if(int(b[g])>=5):
          j=ord(b[i])
          j=j+1
          j=chr(j)
          h+=j
        else:
          h+=b[i]
  elif(nodp>f):
    for i in range(g):
      if(i<c):
        h+=b[i]
      elif(i>=c):
        h+='0'
  else:
    h=b
  print(h)

      
  
