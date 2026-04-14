# Two Pointer Approach

# haystack = "sadbutsad", needle = "sad" o/p 0

haystack = "sadbutsad"
needle = "sad"

m=len(haystack)
n=len(needle)
for i in range(m-n+1):
    if haystack[i:i+n]==needle:
        print(i)
        break