MAX_STACK_SIZE = 256
MAX_QUEUE_SIZE = 256


class Stack:
    def __init__(self):
        self._list = [0] * MAX_STACK_SIZE
        self._pointer = -1

    def push(self, value):
        self._pointer += 1
        self._list[self._pointer] = value

    def pop(self):
        if self._pointer < 0:
            raise IndexError
        retval = self._list[self._pointer]
        self._pointer -= 1
        return retval


class Queue:
    def __init__(self):
        self._list = [0] * MAX_QUEUE_SIZE
        self._pointer = -1

    def push(self, value):
        self._pointer += 1
        for index in range(self._pointer, -1, -1):
            self._list[index + 1] = self._list[index]
        self._list[0] = value

    def pop(self):
        if is_empty():
            raise IndexError
        retval = self._list[self._pointer]
        self._pointer -= 1
        return retval

    def is_empty(self):
        return self._pointer < 0


# Tree
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


# Breadth First Search
def bfs(root, value):
    to_visit = Queue()
    to_visit.push(root)
    while not to_visit.is_empty():
        node = to_visit.pop()
        if node.value == value:
            return node
        for child in node.children:
            to_visit.push(child)
    return None

# Depth First Search


def dfs(root, value):
    if root.value == value:
        return value
    for child in root.children:
        retval = dfs(child, value)
        if retval:
            return retval
    return None


# traversal methods
def pre_order(root):
    if root is None:
        return
    print(root)
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root)


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root)
    in_order(root.right)

# TODO: look into heapify


class Heap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__percolateUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__percolateUp(len(self.heap) - 1)

    def get(self, data):
        for item in self.heap:
            if item == data:
                return True
            else:
                return None

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __percolateUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__percolateUp(parent)

    def __percolateDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__percolateDown(largest)


def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst


def quick_sort_helper(lst, low, hi):
    if hi <= low:
        return

    pivot = partition(lst, low, hi)

    quick_sort_helper(lst, low, pivot - 1)
    quick_sort_helper(lst, pivot + 1, hi)


def partition(lst, low, hi):
    pivot = low

    for i in range(low + 1, hi + 1):
        if lst[i] < lst[pivot]:
            for j in range(i, pivot, -1):
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            pivot += 1
    return pivot


a = [15, 21, 45, 80, 5, 2]
aa = [15, 21, 45, 80, 5, 2]
b = [3, 1, 4, 2, 5]
c = [1, 2, 3, 4, 5]
# d = []
e = [80, 79, 78, 77, 76]


def test_quick_sort():
    assert quick_sort(a) == [2, 5, 15, 21, 45, 80]
    assert quick_sort(b) == [1, 2, 3, 4, 5]
    assert quick_sort(c) == [1, 2, 3, 4, 5]
    # assert quick_sort(d) == []
    assert quick_sort(e) == [76, 77, 78, 79, 80]


def test_partition():
    assert partition(a, 0, 5) == 2
    assert partition(b, 0, 4) == 2
    assert partition(c, 0, 4) == 0
    assert partition(aa, 2, 5) == 4
    assert partition(e, 0, 4) == 4


# test_partition()
test_quick_sort()
