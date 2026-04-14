# Two Pointer Approach

#s = "cat and mice" o/p = "cat dna mice"

s="cat and mice"

s=s.split()
res=[s[0]]

def count_vowels(word):
    return sum(c in "aeiou" for c in word)

count=count_vowels(s[0])

for word in s[1:]:
    if count_vowels(word)==count:
        res.append(word[::-1])
    else:
        res.append(word)
print(" ".join(res))