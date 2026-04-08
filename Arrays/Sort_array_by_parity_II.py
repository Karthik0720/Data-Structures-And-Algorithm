# Two pointer Approach

#nums = [4,2,5,7] o/p = [4,5,2,7]

nums = [4,2,5,7]
even,odd=0,1
while even<len(nums) and odd<len(nums):
    if nums[even]%2==0:
        even+=2
    elif nums[odd]&2==1:
        odd+=2
    else:
        nums[even],nums[odd]=nums[odd],nums[even]
        even+=2
        odd+=2
print(nums)