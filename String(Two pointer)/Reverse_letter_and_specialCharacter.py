# Two Pointer Approach

#s = ")ebc#da@f(" o/p "(f@ad#cbe)"

s=")ebc#da@f("
s=list(s)
l,r=0,len(s)-1
while l<r:
    if not s[l].isalnum():
        l+=1
    elif not s[r].isalnum():
        r-=1
    else:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1

l,r=0,len(s)-1
while l<r:
    if s[l].isalnum():
        l+=1
    elif s[r].isalnum():
        r-=1
    else:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
print("".join(s))
