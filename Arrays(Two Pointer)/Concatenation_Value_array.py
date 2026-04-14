# Two Pointer Approach

#nums = [5,14,13,8,12] o/p=673

nums = [5,14,13,8,12]
res=0
l,r=0,len(nums)-1
while l<r:
    concat=str(nums[l])+str(nums[r])
    res+=int(concat)
    l+=1
    r-=1
if len(nums)%2==1:
    res+=nums[l]
print(res)