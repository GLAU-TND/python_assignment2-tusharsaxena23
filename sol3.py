l=eval(input())
a=0
for i in range(1,len(l)):
    if(l[i-1]>l[i]):
        a+=1
if a<=1:
    print(True)
else:
    print(False)
