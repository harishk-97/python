p=input()
q=len(p)
r=0
for i in range(q):
  if((q!=32)and(q!=46)and((q<47)or(q>58))and((q<64)or(q>91))and((q<96)or(q>123))):
    r=r+1
print(r)    
