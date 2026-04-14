# Two Pointer Approach

#s = "the sky is blue" o/p="blue is sky the"

s = "the sky is blue"

words=[]
word=""

for ch in s:
    if ch!= " ":
        word+=ch
    else:
        if word:
            words.append(word)
            word=""
if word:
    words.append(word)
words.reverse()
print(" ".join(words))