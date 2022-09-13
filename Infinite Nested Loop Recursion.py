
def infinite_loop(n,arr):
    if len(arr)==n:
        print(arr)
        return
    for j in range(n+1):
        infinite_loop(n,arr+[j])

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# for i in range(3)
    #for j in range(3)
        #print(i,j)

# for i in range(4)
    #for j in range(4)
        #for k in range(4)
            #print(i,j,k)

# New task for loop

# for i in range(3)
    #for j in range(3)
        #for k in range(3)
            # for l in range(3)
                # for m in range(3)
                    #print(i,j,k,l,m)

