s=list(input().split())
k=int(input())
c=9
i=0
k=0
for p in s:
    if len(p)>10:
        k+=1
if k==0:
    while i!=len(s):
        if len(s[i])<=c:
            print(s[i],end=" ")
            c=c-len(s[i])
            i+=1
        else:
            print()
            c=9
else:
    print(None)
