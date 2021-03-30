# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        cur = self
        if self == None:
            cur = BST(value)
        while True:
            if value < cur.value:
                if cur.left == None:
                    cur.left = BST(value)
                    break
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = BST(value)
                    break
                else:
                    cur = cur.right
        return self

    def contains(self, value):
        cur = self
        if self == None:
            return False
        else:
            while cur != None:
                if cur.value == value:
                    return True
                else:
                    if value < cur.value:
                        cur = cur.left
                    else:
                        cur = cur.right
            return False

    def remove(self, value):
        cur = self
        p = None
        leftC = None
        while cur != None:
            if cur.value == value:
                # No C
                if cur.left == None and cur.right == None:
                    # no P  do nothing
                    if p == None:
                        pass
                    # P
                    else:
                        # left remove left
                        if leftC:
                            p.left = None
                        # right remove right
                        else:
                            p.right = None
                # only left c
                elif cur.right == None and cur.left != None:
                    # p left p.left = cur.left
                    if leftC:
                        p.left = cur.left
                    # p right pright = cur.left
                    else:
                        p.right = cur.left
                # only right c
                elif cur.left == None and cur.right != None:
                    # p left p.left = cur.right
                    if leftC:
                        p.left = cur.right
                    # p right pright = cur.right
                    else:
                        p.right = cur.right
                # both c
                else:
                    if leftC:
                        p.left.value = cur.left.remove_min()
                    else:
                        p.right.value = cur.left.remove_min()
                # p.left = cur.minleft
                break
            else:
                if value < cur.value:
                    p = cur
                    leftC = True
                    cur = cur.left
                else:
                    leftC = False
                    cur = cur.right

    return self

    def remove_min(self):
        cur = self
        p = None
        res = None
        while cur.left != None:
            p = cur
            cur = cur.left
        res = cur.value
        if p == None:
            cur = None
        else:
            if p.left == cur:
                p.left = None
            else:
                p.right = None
        return res



https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/