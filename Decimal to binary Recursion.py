
def Conv_Bin(n):
    if n == 0 or n==1 : return f'{n}'
    return  Conv_Bin(n//2) + f'{n%2}'

def Back_Conv_Bin(n):
    if n == 0 or n == 1:
        return f"{n}"
    res = Back_Conv_Bin(n//2)
    return res + f'{n%2}'

print(Back_Conv_Bin(112))
