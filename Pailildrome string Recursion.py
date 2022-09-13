
# Method 1 rev and check

def Reverse(string):
    leng = len(string)-1
    if len(string) < 1:
        return ''
    else:
        return string[leng] + Reverse(string[0:leng])

giv_str = "10001"
rev = Reverse(giv_str)
if rev == giv_str:
    print("Palildrome")
else:
    print("not palildrome")


# Method 2 check every mirror element

def Palildrome(string,i,j):
    if i >= j : return True
    if string[i]!=string[j]: return False
    else:
        return Palildrome(string,i+1,j-1)

print(Palildrome(giv_str,0,len(giv_str)-1))