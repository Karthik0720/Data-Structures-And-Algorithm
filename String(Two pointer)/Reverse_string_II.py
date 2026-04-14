# Two Pointer Approach

#s = "abcdefg", k = 2 o/p="bacdfeg"

s = "abcdefg"
s=list(s)
k = 2
for i in range(0,len(s),2*k):
    l=i
    r=min(l+k-1,len(s)-1)
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
print("".join(s))
