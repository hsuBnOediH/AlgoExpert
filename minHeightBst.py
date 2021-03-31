def minHeightBst(array):
    order_array = reorder_array(array)
    print(order_array)


tree = BST(order_array[0])
if len(array) > 1:
    for i in range(1, len(array)):
        tree.insert(order_array[i])
return tree


def reorder_array(array):
    if len(array) == 1: return array
    res = []
    # if len(array) % 2 == 0:
    # else:
    m_i = len(array) // 2
    res.append(array[m_i])

    if m_i + 1 <= len(array) - 1:
        res.extend(reorder_array(array[m_i + 1:]))
    if m_i - 1 >= 0:
        res.extend(reorder_array(array[:m_i]))
    return res


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst(array):
    order_array = reorder_array(array, 0, len(array) - 1)
    print(order_array)


tree = BST(order_array[0])
if len(array) > 1:
    for i in range(1, len(array)):
        tree.insert(order_array[i])
return tree


def reorder_array(array, start, end):
    res = []
    if end < start: return array
    # if len(array) % 2 == 0:
    # else:
    m_i = (start + end) // 2
    res.append(array[m_i])

    if m_i + 1 <= end:
        res.extend(reorder_array(array, m_i + 1, end))
    if m_i - 1 >= start:
        res.extend(reorder_array(array, start, m_i))
    return res


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
# 利用 end start 取代新的array  截断问题