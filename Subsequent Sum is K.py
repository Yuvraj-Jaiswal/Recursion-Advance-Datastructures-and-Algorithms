
elem_arr = [1,2,1,1,2,3,2,1,1]

# Method to Print all answer in recursion
def Sum_Subsequent(arr,i,k):
    global elem_arr
    if i >= len(elem_arr):
        if sum(arr)==k:
            print(arr)
        return None

    arr.append(elem_arr[i])
    Sum_Subsequent(arr,i+1,k)

    arr.pop(len(arr)-1)
    Sum_Subsequent(arr,i+1,k)


# Method to Print only one answer in recursion
def Sum_Subsequent_only1(arr,i,k):
    global elem_arr
    if i >= len(elem_arr):
        if sum(arr)==k:
            print(arr)
            return True
        else:return False

    arr.append(elem_arr[i])
    if Sum_Subsequent_only1(arr, i + 1, k) == True: return True

    arr.pop(len(arr)-1)
    if Sum_Subsequent_only1(arr,i+1,k) == True :return True

    return False


# Count number of subsequent which has sum equal to K
def Sub_sum_count(arr,i,k):
    global elem_arr
    if i >= len(elem_arr):
        if sum(arr) == k :
            return 1
        else:return 0

    arr.append(elem_arr[i])
    l = Sub_sum_count(arr,i+1,k)

    arr.pop(len(arr)-1)
    r = Sub_sum_count(arr,i+1,k)

    return l+r

print(Sub_sum_count([],0,2))

