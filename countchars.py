s=input()
d={}
if s.isspace():
    print("empty")
elif s.isdigit():
    print("char")
else:
    for i in s:
        d[i]=s.count(i)
    print(d)