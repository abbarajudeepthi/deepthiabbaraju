def vowel(s):
    x='aeiou'
    for ele in s:
        if ele in x:
            return True
        else:
            return False
s=input()
res=vowel(s)
if res==True:
    print("cv")
else:
    print("dncv")