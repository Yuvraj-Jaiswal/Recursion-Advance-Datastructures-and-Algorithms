
def Rev_Arr(arr , i , j):
    if i >= j:
        print(arr)
        return None
    else:
        arr[i] , arr[j] = arr[j] , arr[i]
        Rev_Arr(arr,i+1,j-1)

arr1 = [1,2,3,4,5,6]
Rev_Arr(arr1,0,len(arr1)-1)