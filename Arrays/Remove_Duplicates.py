# Two poiter Approach 

#nums = [1,1,2] o/p=[1,2]

nums=[1,1,2]
l,r=1,1
while r<len(nums):
    if nums[r]!=nums[r-1]:
        nums[l]=nums[r]
        l+=1
        r+=1
    else:
        r+=1
print(nums[:l])