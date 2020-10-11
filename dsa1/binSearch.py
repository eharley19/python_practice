def find_index(lst, item):
    for index, elem in enumerate(lst):
        if elem == item:
            return index
    return -1


def binary_search(lst, item):
    if len(lst) == 0:
        return -1

    mid = len(lst) // 2
    if lst[mid] == item:
        return mid
    if lst[mid] > item:
        return binary_search(lst[:mid], item)
    else:
        return binary_search(lst[mid + 1:], item)
