initial=int(input())
stair=input().split()
stair=list(map(int,stair))
book=[]
for i in range(1,initial):
  note=0
  for j in range(i):
    if(stair[i]>stair[j]):
      note=note+stair[j]
  book.append(note)
print(sum(book))
