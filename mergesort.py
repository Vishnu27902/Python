def mergeSort(ls,start,end):
    if(start<end):
        mid=(start+end)//2
        mergeSort(ls,start,mid)
        mergeSort(ls,mid+1,end)
        combine(ls,start,end,mid)
def combine(ls,start,end,mid):
    i,j,temp=start,mid+1,0
    mls=[]
    while(i<=mid and j<=end):
        if(ls[i]>ls[j]):
            mls.append(ls[j])
            j+=1
            temp+=1
        else:
            mls.append(ls[i])
            i+=1
            temp+=1
        # print(mls)
    while(i<=mid):
        mls.append(ls[i])
        i+=1
        temp+=1
    while(j<=end):
        mls.append(ls[j])
        j+=1
        temp+=1
    for z in range(start,end+1):
        ls[z]=mls[z-start]
a=[9,7,6,5,4,3,2,1]
mergeSort(a,0,len(a)-1)
print(a)