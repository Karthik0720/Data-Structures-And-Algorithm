# Two pointer Approach

#nums = [0,1,0,3,12] o/p = [1,3,12,0,0]

nums = [0,1,0,3,12]

p=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[i],nums[p]=nums[p],nums[i]
        p+=1
print(nums)