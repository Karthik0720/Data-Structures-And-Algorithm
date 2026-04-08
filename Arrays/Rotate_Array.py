# Two pointer Approach

#nums = [1,2,3,4,5,6,7], k = 3 o/p = [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
k = 3
n=len(nums)
k=k%n

def rotate(l,r):
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
rotate(0,n-1)
rotate(0,k-1)
rotate(k,n-1)
print(nums)
