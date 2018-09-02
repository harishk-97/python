a=list(input())
if 'd' in a and 'h' in a and 'o' in a and 'n' in a and 'i' in a:
  a.remove('d')
  a.remove('h')
  a.remove('o')
  a.remove('n')
  a.remove('i')
if not a:
  print('yes')
else:
  print('no')
