names={}
n=int(input())
for i in range(n):
    names[i+1]=input("name")
name=list(names.values())
p=int(input("Position"))
name.sort(key=lambda x:x[p-1])
print(name)