# Two pointer Approach

#nums = [3,1,2,4] o/p = [2,4,3,1]

nums = [3,1,2,4]
even=0
for i in range(len(nums)):
    if nums[i]%2==0:
        nums[even],nums[i]=nums[i],nums[even]
        even+=1
print(nums)