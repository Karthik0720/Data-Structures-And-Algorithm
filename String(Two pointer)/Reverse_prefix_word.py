# Two pointer approach

#word = "abcdefd", ch = "d" o/p = "dcbaefd"

word = "abcdefd"
ch = "d"
s=list(word)
for i in range(len(s)):
    if s[i]==ch:
        l=0
        r=i
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        break
print("".join(s)) 