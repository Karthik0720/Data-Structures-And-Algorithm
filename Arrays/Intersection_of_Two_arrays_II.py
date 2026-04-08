# Two pointer Approach

#nums1 = [1,2,2,1], nums2 = [2,2] o/p = [2,2]

nums1 = [1,2,2,1]
nums2 = [2,2]
nums1.sort() and nums2.sort()
i=j=0
res=[]
while i<len(nums1) and j<len(nums2):
    if nums1[i]==nums2[j]:
        res.append(nums1[i])
        i+=1
        j+=1
    elif nums1[i]<nums2[j]:
        i+=1
    else:
        j+=1
print(res)

# if output want to unique print(list(set(res))) o/p= [2]