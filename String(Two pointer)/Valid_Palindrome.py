# Two pointer Appoarch

# s = "A man, a plan, a canal: Panama" o/p=True

s = "A man, a plan, a canal: Panama"
l,r=0,len(s)-1
while l<r:
    if not s[l].isalnum():
        l+=1
    elif not s[r].isalnum():
        r-=1
    else:
        if s[l].lower()!=s[r].lower():
            print(False)
            break
        l+=1
        r-=1
else:
    print(True)