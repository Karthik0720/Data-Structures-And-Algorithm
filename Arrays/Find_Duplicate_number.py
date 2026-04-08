# Two pointer Approach

#nums = [1,3,4,2,2] o/p = 2

nums = [1,3,4,2,2]
seen=set()
for num in nums:
    if num in seen:
        print(num)
    seen.add(num)

