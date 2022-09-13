# --- parameters ---
# position -> no of positions in which given elements can be filled
# value_arr -> array of elements which we can use ( which can be placed at given locations )
# repeatation_allow -> it is an boolian which specify can we repeat elements or not ( T or F )

def Permutation_in_elements(positions,value_arr,repeatation_allow,arr=[],seen=[]):
    if len(arr)==positions:
        print(arr)
        return

    for j in range(len(value_arr)):
        if not repeatation_allow:
            if j not in seen:
                Permutation_in_elements(positions,value_arr,repeatation_allow,arr+[value_arr[j]],seen+[j])
        else:
            Permutation_in_elements(positions,value_arr,repeatation_allow,arr+[value_arr[j]] ,seen+[j])


val_arr = [1,2,3]
Permutation_in_elements(positions=3 , value_arr=val_arr , repeatation_allow=False)