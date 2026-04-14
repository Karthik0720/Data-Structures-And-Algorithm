# Two pointer Approach

#nums = [1,1,1,2,2,3] o/p = [1,1,2,2,3]

nums = [1,1,1,2,2,3]
p=2
for i in range(2,len(nums)):
    if nums[i]!=nums[p-2]:
        nums[p]=nums[i]
        p+=1
print(nums[:p])