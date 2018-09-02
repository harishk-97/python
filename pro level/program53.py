s=input().split()
a=[]
for i in range(len(s)):
  for j in range(len(s[i])):
    if(ord(s[i][j])>96 and ord(s[i][j])<123):
      if (ord(s[i][j])-96) not in a:
        a.append((ord(s[i][j])-96))
    elif(ord(s[i][j])>64 and ord(s[i][j])<91):
      if (ord(s[i][j])-64) not in a:
        a.append((ord(s[i][j])-6))
if(sum(a)==351):
  print('yes')
else:
  print('no')
