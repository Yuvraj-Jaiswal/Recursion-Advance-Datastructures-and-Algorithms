
# Backtracking Printing
def Rev_string(st):
    if len(st) < 1:
        return

    Rev_string(st[1:len(st)])
    print(st[0],end="")

# Recursion
def Rev_string_idx(st):
    if len(st) < 1:
        return ''

    return st[len(st)-1] + Rev_string_idx(st[0:len(st)-1])

# Reversed Recursion
def Rev_recursion(st):
    if len(st) < 1 : return ''
    return Rev_recursion(st[1:len(st)]) + st[0]

print(Rev_recursion("abcdef"))