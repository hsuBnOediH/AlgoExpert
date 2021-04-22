# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    one = linkedListOne
    two = linkedListTwo
    tol = one.value + two.value
    digit = tol % 10
    remain = tol // 10
    res = LinkedList(digit)

    cur_o = one.next
    cur_t = two.next
    cur_r = res
    # while 的逻辑判断是相反的 注意多段的时候 是 and或者or
    while cur_o is not None or cur_t is not None:
        if cur_o is None:
            tol = cur_t.value + remain
            cur_t = cur_t.next
        elif cur_t is None:
            tol = cur_o.value + remain
            cur_o = cur_o.next
        else:
            tol = cur_t.value + cur_o.value + remain
            cur_t = cur_t.next
            cur_o = cur_o.next
        digit = tol % 10
        remain = tol // 10
        cur_r.next = LinkedList(digit)
        cur_r = cur_r.next
    if remain != 0:
        cur_r.next = LinkedList(remain)
    return res
