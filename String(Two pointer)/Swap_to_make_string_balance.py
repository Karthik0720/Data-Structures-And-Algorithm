# Two Pointer Approach

#s = "][][" o/p = 1

s = "][]["

balance=0
imbalance=0
for ch in s:
    if ch=="[":
        balance+=1
    else:
        if balance>0:
            balance-=1
        else:
            imbalance+=1
print((imbalance+1)//2)