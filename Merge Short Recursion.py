
def Merge_arr(left,right):
    i = 0
    j = 0
    merge_arr = []

    while i <= len(left) and j <= len(right):

        if i == len(left):
            merge_arr += right[j:len(right)]
            break

        if j == len(right):
            merge_arr += left[i:len(left)]
            break

        if left[i] < right[j]:
            merge_arr.append(left[i])
            i += 1
        else:
            merge_arr.append(right[j])
            j += 1

    return merge_arr


def Merge_Short(arr):
    if len(arr) <= 1 : return arr

    mid = (len(arr))//2

    left = Merge_Short(arr[0:mid])
    right = Merge_Short(arr[mid:len(arr)])

    return Merge_arr(left,right)

print(Merge_Short([10,4,7,5,2,1,13]))

