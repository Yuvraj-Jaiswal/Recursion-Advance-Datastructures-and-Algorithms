
def transfer_hanoi(s,d):
    elm = s[len(s)-1]
    d.append(elm)
    s.pop(len(s)-1)

def tower_of_hanoi(sorc , hel , dest, n):

    if n==0 :
        transfer_hanoi(sorc,dest)
        print(sorc, hel, dest)
        return

    tower_of_hanoi(sorc,dest,hel, n-1)
    print(sorc,hel,dest)
    transfer_hanoi(sorc, dest)
    tower_of_hanoi(hel,sorc,dest, n-1)

tower_of_hanoi([4,3,2,1] , [] , [] , 2)