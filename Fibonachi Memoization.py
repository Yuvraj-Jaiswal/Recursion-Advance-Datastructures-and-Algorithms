
fib_dir = {0:0 , 1:1}

def Memoized_Fib(n):
    if n in fib_dir:
        return fib_dir[n]

    else:
        result = Memoized_Fib(n-1)+Memoized_Fib(n-2)
        fib_dir[n] = result
        return result

print(Memoized_Fib(32))
print(fib_dir)