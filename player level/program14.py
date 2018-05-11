a=input()
c=''
d=[97,101,105,111,117,65,69,73,79,85]
for i in range(len(a)):
  b=ord(a[i])
  if b not in d:
    c+=a[i]
print(c[::-1])
  
  
