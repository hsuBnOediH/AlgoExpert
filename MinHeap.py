# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # index 问题 heap 不能直接call？？ 尽量传递变量！
    def buildHeap(self, array):
        last_p = (len(array) - 2) // 2
        for idx in reversed(range(last_p + 1)):
            self.siftDown(idx, len(array) - 1, array)
        return array

    def siftDown(self, idx, end, heap):
        c1 = idx * 2 + 1
        while c1 <= end:
            # 符号顺序错误
            c2 = c1 + 1 if c1 + 1 <= end else -1
            if c2 != -1 and heap[c1] > heap[c2]:
                swap_idx = c2
            else:
                swap_idx = c1
            if heap[swap_idx] < heap[idx]:
                self.swap(heap, swap_idx, idx)
                idx = swap_idx
                # 忘记 +1
                c1 = idx * 2 + 1
            else:
                break
        # Write your code here.

    pass

    def siftUp(self, idx, heap):
        parent = (idx - 1) // 2
        # 等于号码! parent 为 0 需要比较
        # while parent >= 0 and self.heap[parent] > self.heap[idx]:
        # cur只用关注到第二城, 2nd idx = 1 或者2, par 不可能小于0
        while parent >= 0 and heap[parent] > heap[idx]:
            self.swap(heap, parent, idx)
            #  self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        # res = self.heap[0]
        # last = self.heap.pop()
        # self.heap[0] = last
        self.swap(self.heap, 0, len(self.heap) - 1)
        res = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return res

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]
