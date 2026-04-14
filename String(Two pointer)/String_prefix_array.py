# Two Pointer Approach

#s = "iloveleetcode", words = ["i","love","leetcode","apples"] o/p=True

s = "iloveleetcode"
words = ["i","love","leetcode","apples"]

i=0
for word in words:
    for ch in word:
        if i>=len(s) or s[i]!=ch:
            print(False)
            break
        i+=1
    if i==len(s):
        print(True)
        break
