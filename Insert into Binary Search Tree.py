class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

n1 = Tree(100)
n2 = Tree(120)
n3 = Tree(132)
n4 = Tree(80)
n5 = Tree(50)
n6 = Tree(90)
n7 = Tree(110)

n1.right = n2
n1.left = n4
n2.right = n3
n2.left = n7
n4.right = n6
n4.left = n5


def Inser_node(root,n):
    if root is None:
        r = Tree(n)
        return r

    if root.val < n:
        root.right = Inser_node(root.right,n)
    else:
        root.left = Inser_node(root.left,n)

    return root