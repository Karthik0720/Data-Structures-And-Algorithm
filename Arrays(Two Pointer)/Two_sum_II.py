# Two pointer Approach

#numbers = [2,7,11,15], target = 9 o/p = [1,2]

numbers=[2,7,11,15]
target=9
l,r=0,len(numbers)-1
while l<r:
    s=numbers[l]+numbers[r]
    if s==target:
        print([l+1,r+1])
        break
    elif s<target:
        l+=1
    else:
        r-=1
else:
    print(-1)

