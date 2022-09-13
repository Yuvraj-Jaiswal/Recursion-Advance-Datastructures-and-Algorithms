
arr_elem = [3,1,2,5,6]

def Subsequent(arr,i):
    global arr_elem
    if i >= len(arr_elem):
        print(arr)
        return None

    arr.append(arr_elem[i])
    Subsequent( arr , i+1)

    arr.pop(len(arr)-1)
    Subsequent(arr , i+1)

sub_sequent = []
Subsequent(sub_sequent,0)

