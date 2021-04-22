# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        # Write your code here.

    pass

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        # Write your code here.

    pass

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        cur_p = 1
        while node is not None and cur_p != position:
            node = node.next
            cur_p += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)

    else:
    self.setTail(nodeToInsert)


def removeNodesWithValue(self, value):
    cur = self.head
    while cur is not None:
        remove = cur
        cur = cur.next

        if remove.value == value:
            self.remove(remove)
    # else:


def remove(self, node):
    if node == self.head:
        self.head = self.head.next
    if node == self.tail:
        self.tail = self.tail.prev
    self.remove_bind(node)


def remove_bind(self, cur):
    if cur.next is not None:
        cur.next.prev = cur.prev
    if cur.prev is not None:
        cur.prev.next = cur.next
    cur.prev = None
    cur.next = None


def containsNodeWithValue(self, value):
    res = False
    cur = self.head
    while cur != None:
        if cur.value == value:
            res = True
            break
        else:
            cur = cur.next
    return res
