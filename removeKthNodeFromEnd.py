# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    length = 1
    cur = head
    while cur.next != None:
        cur = cur.next
        length += 1

    target = length - k
    cur = head
    if target == 0:
        # head = head.next
        # cur.next = None
        # cur.next = None
        # 不能改变def 的 parameter, 所以把2的value copy 到1 然后删除2
        head.value = head.next.value
        head.next = head.next.next
    else:
        idx = 0
        while idx + 1 != target:
            cur = cur.next
            idx += 1
        remove = cur.next
        cur.next = cur.next.next
        remove.next = None


# sigle linklist 利用单个指针的方法 找end idx
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    idx = 0
    f = head
    s = head
    while idx != k:
        f = f.next
        idx += 1
    # print(f.value)
    if f is None:
        head.value = head.next.value
        head.next = head.next.next
    else:
        while f.next is not None:
            f = f.next
            s = s.next
        s.next = s.next.next

