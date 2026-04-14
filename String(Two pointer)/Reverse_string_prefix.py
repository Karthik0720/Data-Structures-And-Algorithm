# Two Pointer Approach

#s = "abcd", k = 2 o/p "bacd"

s="abcd"
k=2
s=list(s)
l,r=0,k-1
while l<r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1
print("".join(s))