a=[57,2,6,49,43]
for i in range(1,len(a)):
    j=i-1
    nele=a[i]
    while a[j]>nele and j>=0:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=nele
print(a)