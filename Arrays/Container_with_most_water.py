# Two pointer Approach

# height = [1,8,6,2,5,4,8,3,7] o/p = 49

height=[1,8,6,2,5,4,8,3,7]
max_vol=0
l,r=0,len(height)-1
while l<r:
    distance=r-l
    mini=min(height[l],height[r])
    vol=distance*mini
    max_vol=max(max_vol,vol)
    if height[l]<height[r]:
        l+=1
    else:
        r-=1
print(max_vol)
