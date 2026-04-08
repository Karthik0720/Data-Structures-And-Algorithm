# Two pointer approach

#nums = [3,2,2,3] o/p=[2,2]

nums=[3,2,2,3]
val=3
p=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[p]=nums[i]
        p+=1
print(nums[:p])