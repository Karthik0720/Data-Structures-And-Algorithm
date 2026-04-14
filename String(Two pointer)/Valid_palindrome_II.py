# Two Pointer Approach

#s = "abca" o/p=True

s = "abca"
def palindrome(l,r):
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
l,r=0,len(s)-1
while l<r:
    if s[l]!=s[r]:
        print(palindrome(l+1,r) or palindrome(l,r-1))
    l+=1
    r-=1
print(True)
        