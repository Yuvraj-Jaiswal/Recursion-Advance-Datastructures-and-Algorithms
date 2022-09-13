key_map = {'1':"abc",'2':"def",'3':"ghi",'4':"jkl",'5':"mno"}

def keypad_combination(key_map,st,n_st,i):
    if len(n_st)==len(st):
        print(n_st)
        return

    elems = key_map[f'{st[i]}']
    for elm in elems:
        keypad_combination(key_map,st,n_st+elm,i+1)

keypad_combination(key_map,"2345","",0)
