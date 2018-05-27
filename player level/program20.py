garou=input()
garou=list(map(str,garou))
for i in garou:
  a=ord(i)
  a=a+3
  if(a>90):
    a=a%90
    a=a+64
  print(chr(a),end='')
