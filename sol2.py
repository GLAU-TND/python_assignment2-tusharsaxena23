l=eval(input())
k=int(input())
c=0
for i in range(len(l)):
    a=0
    for j in range(len(l)):
        if j>i:
            a+=l[j]
            if a>k:
                break
            if a==k:
                print(l[i+1:j+1])
                c=1
    if c==1:
        break
if c==0:
    print(None)
