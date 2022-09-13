def Binary_Search(arr,i,j,targ):
    mid = (i+j)//2

    if arr[mid]==targ:
        return True

    if i >= j:
        return False

    if arr[mid] > targ:
        return Binary_Search(arr,i,mid-1,targ)
    else:
        return Binary_Search(arr,mid+1,j,targ)


print(Binary_Search([1,2,3,4,5,6,7],0,6,3))
