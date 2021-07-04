def binarysearch(a,target):
    l=0
    r=len(a)-1
    while(l<=r):
        mid=(l+r)//2
        if(a[mid]==target):
            return mid
        elif(a[mid]<target):
            l=mid+1
        else:
            r=mid-1
    return -1

a=[-2,3,4,7,8,9,11,13]
target=7
result=binarysearch(a,target)

if(result!=-1):
    print(f"Element is present at",result)
else:
    print(f"Element is not present")