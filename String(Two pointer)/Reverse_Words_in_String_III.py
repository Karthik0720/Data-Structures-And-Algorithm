# Two Pointer Approach

#s = "Let's take LeetCode contest" o/p="s'teL ekat edoCteeL tsetnoc"

s = "Let's take LeetCode contest"
res=[]
s=s.split()
for word in s:
    res.append(word[::-1])
print(" ".join(res))