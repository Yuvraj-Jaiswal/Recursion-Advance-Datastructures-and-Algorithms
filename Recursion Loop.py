
def Print_rec(st,en):
    if st>en:
        return
    print(f"hellow {st}")
    Print_rec(st+1,en)

Print_rec(1,10)