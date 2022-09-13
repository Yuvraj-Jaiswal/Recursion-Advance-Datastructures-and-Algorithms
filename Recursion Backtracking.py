
def Print_Rev(st):
    if st < 1:
        return
    Print_Rev(st-1)
    print(st)


Print_Rev(9)
