
# Global Variable Method

result = 0
def Sum_n(num):
    global result
    if num < 1 :
        return None
    Sum_n(num-1)
    # print(f" {result} + {num} = {result+num} ")
    result += num

Sum_n(10)
print(result)

# Parameter Printing Method

def Sum_para(num,res=0):
    if num < 1 :
        print(res)
        return
    Sum_para(num-1,res+num)

Sum_para(10)


# Return Method IMP

def Sum_num(num):
    if num == 0:
        return 0
    else:
        return num+Sum_num(num-1)

ret_res = Sum_num(10)
print(ret_res)