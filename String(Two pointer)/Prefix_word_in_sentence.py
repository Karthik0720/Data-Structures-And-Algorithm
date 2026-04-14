# Two Pointer Approach

#sentence = "i love eating burger", searchWord = "burg" o/p=4

sentence = "i love eating burger"
searchWord = "burg"

s=sentence.split()
for i,word in enumerate(s):
    if word.startswith(searchWord):
        print(i+1)
