def binarySearch(ls,left,right,target):
    mid=(left+right)//2
    # print(mid)
    # print(ls[mid])
    # print(left,right)
    if(left<=right):
        if(target==ls[mid]):
            return mid
        if(target<ls[mid]):
            return binarySearch(ls,left,mid-1,target)
        else:
            return binarySearch(ls,mid+1,right,target)
    return -1
a=[1,2,3,4,5,6,7,8,9,10]
# print(a[6])
print(binarySearch(a,0,len(a)-1,11))
