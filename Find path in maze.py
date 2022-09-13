

def find_path(n,m,pos=[0,0],path=[[0,0]]):
    if pos == [n,m]:
        print("position reached" , path)
        return 1

    if pos[0] > n : return 0
    if pos[1] > m : return 0

    pos[0] = pos[0]+1
    w1 = find_path(n,m,pos,path+[[pos[0],pos[1]]])
    pos[0] = pos[0]-1

    pos[1] = pos[1]+1
    w2 = find_path(n,m,pos,path+[[pos[0],pos[1]]])
    pos[1] = pos[1]-1

    return w1+w2


print(find_path(2,3))