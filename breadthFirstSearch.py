# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = []
        q.append(self)
        while len(q) != 0:
            node = q.pop(0)
            array.append(node.name)
            q.extend(node.children)
        return array
