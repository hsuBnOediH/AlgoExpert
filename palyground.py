# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def removeDuplicatesFromLinkedList(linkedList):
    cur_node = linkedList

    while cur_node != None:
        next_node = cur_node.next
        if next_node != None and cur_node.value == next_node.value:
            temp = next_node.next
            cur_node.next == temp
        else:
            cur_node = cur_node.next


    return linkedList



# [1, 3, 4, 4, 5, 5, 6, 6]
temp = LinkedList(6, None)
temp1 = LinkedList(6, temp)
temp2 = LinkedList(5, temp1)
temp3 = LinkedList(5, temp2)
temp4 = LinkedList(4, temp3)
temp5 = LinkedList(4, temp4)
temp6 = LinkedList(3, temp5)
temp7 = LinkedList(1, temp6)

removeDuplicatesFromLinkedList(temp7)

