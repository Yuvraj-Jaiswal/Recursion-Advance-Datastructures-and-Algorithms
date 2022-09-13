
class Link_List:
    def __init__(self,value):
        self.next = None
        self.value = value

a = Link_List(1)
b = Link_List(2)
c = Link_List(3)
d = Link_List(4)
e = Link_List(5)

a.next = b
b.next = c
c.next = d
d.next = e

def Print_Link_l(head):
    if head is None:
        print("None")
        return
    else: print(f'{head.value} -> ' , end="")
    Print_Link_l(head.next)


def Link_list_rev(head):
    if head.next is None:return head

    h =  Link_list_rev(head.next)
    h.next = head
    head.next = None
    return head


Print_Link_l(a)
Link_list_rev(a)
Print_Link_l(e)