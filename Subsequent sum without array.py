
elem_arr = [1,2,1,1,2,3,2,1,1]

# Without Datastructure
def Sub_sum_count_wd(i, s, k):
    global elem_arr
    if i >= len(elem_arr):
        if s == k:
            return 1
        else:return 0

    s += elem_arr[i]
    l = Sub_sum_count_wd(i + 1, s, k)

    s -= elem_arr[i]
    r = Sub_sum_count_wd(i + 1, s, k)

    return l + r

print(Sub_sum_count_wd(0, 0, 2))