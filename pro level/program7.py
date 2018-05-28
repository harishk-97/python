initial=int(input())
by=0
while initial>2:
    if(initial%2==0):
        initial=initial/2
    else:
        by+=1
        initial=((initial-1)/2)
        initial=initial+1
print(by)
    
