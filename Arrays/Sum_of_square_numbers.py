# Two pointer Approach

#c=5 o/p= True ==> 1*1 + 2*2 = 5

c=5
l,r=0,int(c**0.5)
while l<=r:
    s=l*l+r*r
    if s==c:
        print(True)
        break
    elif s<c:
        l+=1
    else:
        r-=1
else:
    print(False)