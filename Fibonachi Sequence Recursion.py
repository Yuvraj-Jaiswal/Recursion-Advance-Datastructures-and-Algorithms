
def Fubinachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fubinachi(n-1)+Fubinachi(n-2)

print(Fubinachi(4))