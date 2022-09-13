
elem_arr = [10,1,2,7,6,1,5]
result = []

def Comb_Sum(arr,tar,i,cand_arr):
    global result
    if i >= len(cand_arr):
        if tar==0:
            if sorted(arr) not in result:
                result.append(sorted(arr))
        return

    if cand_arr[i] <= tar:
        arr.append(cand_arr[i])
        Comb_Sum(arr,tar-cand_arr[i],i+1,cand_arr)
        arr.pop(len(arr)-1)

    Comb_Sum(arr,tar,i+1,cand_arr)

Comb_Sum([],8,0,elem_arr)
print(result)