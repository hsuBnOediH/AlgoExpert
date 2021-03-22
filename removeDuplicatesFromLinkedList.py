# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    cur_node = linkedList

    while cur_node != None:
        next_node = cur_node.next
        if next_node != None and cur_node.value == next_node.value:
            temp = next_node.next
            # 双等号的问题 有点气人
            # cur_node.next == temp
            cur_node.next = temp
        else:
            cur_node = cur_node.next


    return linkedList


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    cur_node = linkedList

    while cur_node is not None:
        next_diff_node = cur_node.next
        # 利用内嵌的while loop 减少remove的次数
        # 实际上不改变复杂度
        while next_diff_node is not None and next_diff_node.value == cur_node.value:
            temp = next_diff_node.next
            next_diff_node = temp
        cur_node.next = next_diff_node
        cur_node = next_diff_node


    return linkedList

