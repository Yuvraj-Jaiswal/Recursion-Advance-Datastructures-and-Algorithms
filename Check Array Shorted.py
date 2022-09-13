
def Check_arr_shorted(arr,i=0,j=1):
    if j == len(arr): return True

    if arr[j] < arr[i]:
        return False

    ans = Check_arr_shorted(arr,i+1,j+1)
    return ans

elm = [1,2,3,40,50,90,60,70]
print(Check_arr_shorted(elm))