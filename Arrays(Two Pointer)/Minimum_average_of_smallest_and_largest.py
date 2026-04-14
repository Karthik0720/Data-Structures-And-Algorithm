# Two pointer Approach

#nums = [7,8,3,4,15,13,4,1] o/p=5.5

nums = [7,8,3,4,15,13,4,1]
nums.sort()
mini=float('inf')
l,r=0,len(nums)-1
while l<r:
    avg=(nums[l]+nums[r])/2.0
    mini=min(mini,avg)
    l+=1
    r-=1
print(mini)