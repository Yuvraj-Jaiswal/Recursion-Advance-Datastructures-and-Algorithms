
arr_elem = [1,2,3]

def Combination_sum(arr,tar,i):
    global arr_elem
    if i >= len(arr_elem):
        if tar == 0:print(arr)
        return

    if arr_elem[i] <= tar:
        arr.append(arr_elem[i])
        Combination_sum(arr,(tar-arr_elem[i]),i)
        arr.pop(len(arr)-1)

    Combination_sum(arr,tar,i+1)

Combination_sum([],4,0)
