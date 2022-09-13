
class Link_List:
    def __init__(self,value):
        self.next = None
        self.value = value

a = Link_List(1)
b = Link_List(5)
c = Link_List(8)
d = Link_List(40)
e = Link_List(70)

a.next = b
b.next = c
c.next = d
d.next = e


f = Link_List(2)
g = Link_List(6)
h = Link_List(25)
i = Link_List(90)

f.next = g
g.next = h
h.next = i

def Print_Link_l(head):
    if head is None:
        print("None")
        return
    else: print(f'{head.value} -> ' , end="")
    Print_Link_l(head.next)


def Merge_Link_list(h1 , h2):
    if h1 is None: return h1
    if h2 is None: return h2

    if h1.value < h2.value:
        h1.next = Merge_Link_list(h1.next,h2)
        return h1
    else:
        h2.next = Merge_Link_list(h1,h2.next)
        return h2








    pass


Merge_Link_list(a,f)