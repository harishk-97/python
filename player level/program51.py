m=int(input())
n=input().split()
n=list(map(int,n))
n.remove(min(n))
print(min(n))
