
# complicated backtracking solution
def Permute(st,i,arr,seen):
    
    if len(arr)==len(st):
        print(arr)
        return arr

    for j in range(0,len(st)):
        if j not in seen:
            arr.append(st[j])
            seen.append(j)
            Permute(st,i+1,arr,seen)
            seen.pop(len(seen)-1)
            arr.pop(len(arr)-1)


#Easy permutation of string

def permutaion(st,n_st="",seen=[]):
    if len(n_st) == len(st):
        print(n_st)
        return

    for j in range(len(st)):
        if j not in seen:
            permutaion(st,n_st+st[j],seen+[j])

permutaion("abc")