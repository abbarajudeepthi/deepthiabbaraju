def words(word):
    count=0
    l=['a','k','e','o','t','p','n']
    word=list(word)
    for ch in range(len(word)):
        for i in range(len(l)):
            if word[ch]==l[i]:
                count+=1
    return count
word=input()
w=word.lower()
r=words(w)
if r==len(word):
    print("contain all letters")
else:
    print("does not contains all letters")