
def Subsequence(st,i,n_st):
    if i == len(st):
        print(n_st)
        return
    # to be chosen
    Subsequence(st,i+1,n_st+st[i])
    # to be not chosen
    Subsequence(st,i+1,n_st)


def Unique_sub_Seq(st,i,n_st,u_set):
    if i == len(st):
        u_set.add(n_st)
        return

    Unique_sub_Seq(st,i+1,n_st+st[i],u_set)
    Unique_sub_Seq(st,i+1,n_st,u_set)

u_set_sub = set()
Unique_sub_Seq("abc",0,"",u_set_sub)
print(u_set_sub)
