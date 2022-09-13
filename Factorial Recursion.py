
# Return Method

def Fact(n):
    if n==0:
        return 1
    else:
        return n*Fact(n-1)
print(Fact(4))

# Parameter Method

def Fact_para(n,res=1):
    if n < 1:
        print(res)
        return
    Fact_para(n-1,res*n)

Fact_para(5)