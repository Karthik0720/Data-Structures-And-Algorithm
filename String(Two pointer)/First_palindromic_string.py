# Two Pointer Approach

#words = ["abc","car","ada","racecar","cool"] o/p = "ada"

words = ["abc","car","ada","racecar","cool"]

for word in words:
    if word==word[::-1]:
        print(word)
        break