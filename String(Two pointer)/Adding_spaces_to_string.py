# Two Pointer Approach

#s = "LeetcodeHelpsMeLearn", spaces = [8,13,15] o/p = "Leetcode Helps Me Learn"

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

res=[]
l=0
for i in range(len(s)):
    if l<len(spaces) and i==spaces[l]:
        res.append(" ")
        l+=1
    res.append(s[i])
print("".join(res))