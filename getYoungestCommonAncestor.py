# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    a_set = set()
    cur = descendantOne
    while cur is not None:
        a_set.add(cur.name)
        cur = cur.ancestor
    cur = descendantTwo
    while cur is not None:
        if cur.name in a_set:
            return cur
        else:
            cur = cur.ancestor
    return topAncestor


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d_1 = get_d(topAncestor, descendantOne)
    d_2 = get_d(topAncestor, descendantTwo)
    cur_1 = topAncestor
    cur_2 = descendantOne
    diff = d_1 - d_2
    if diff != 0:
        if d_1 > d_2:
            while diff > 0:
                cur_1 = cur_1.ancestor
                diff -= 1
        else:
            while diff > 0:
                cur_2 = cur_2.ancestor
                diff += 1
    while cur_1 is not topAncestor:
        if cur_1 == cur_2:
            return cur_1
        else:
            cur_1 = cur_1.ancestor
            cur_2 = cur_2.ancestor
    return topAncestor


def get_d(root, child):
    res = 0
    cur = child
    while cur is not root:
        res += 1
        cur = cur.ancestor
    return res
