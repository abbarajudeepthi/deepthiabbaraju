def binarysearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
l=[]
n=int(input())
for i in range(n):
    ele=int(input())
    l.append(ele)
low=0
high=n-1
key=int(input("key"))
result=binarysearch(l,low,high,key)
if result==-1:
    print("enf")
else:
    print("ef",result)
