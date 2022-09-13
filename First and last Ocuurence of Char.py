
def FL_occurence(st,char,i=0,f=-1,l=-1):
    if i == len(st) : return [f,l]

    if st[i]==char:
        if f == -1:f = i
        l = i

    idx = FL_occurence(st,char,i+1,f,l)
    return idx

print(FL_occurence("bcbdadf" ,'d'))