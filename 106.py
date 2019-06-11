ax=list(map(int,input().split()))
k=ax[1]
c=s=0
bx=list(map(int,input().split()))
for i in bx:
    if i%2!=0:
        c=i
        s=s+1
    if s==k:
        break
print(c)
