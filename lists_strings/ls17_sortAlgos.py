def selection_sort(lst):
    lst_length = range(len(lst) - 1)
    for i in lst_length:
        min_index = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst


def insertion_sort(lst):
    lst_length = range(1, len(lst))
    for i in lst_length:
        while lst[i - 1] > lst[i] and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i - 1
    return lst


def bubble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def merge_sort(lst):
    merge_sort_helper(lst, 0, len(lst) - 1)
    return lst


def merge_sort_helper(lst, top, bottom):
    if top == bottom:
        return

    middle = (top + bottom) // 2
    merge_sort_helper(lst, top, middle)
    merge_sort_helper(lst, middle + 1, bottom)

    temp_list = []
    index1 = top
    index2 = middle + 1
    while index1 < middle + 1 or index2 < bottom + 1:
        if index1 > middle:
            temp_list.append(lst[index2])
            index2 += 1
        elif index2 > bottom:
            temp_list.append(lst[index1])
            index1 += 1
        elif lst[index1] < lst[index2]:
            temp_list.append(lst[index1])
            index1 += 1
        else:
            temp_list.append(lst[index2])
            index2 += 1
    lst[top:bottom + 1] = temp_list


def test_sorts():
    assert bubble_sort([3, 8, 4, 7, 255, 1]) == [1, 3, 4, 7, 8, 255]
    assert selection_sort([3, 8, 4, 7, 255, 1]) == [1, 3, 4, 7, 8, 255]
    assert insertion_sort([3, 8, 4, 7, 255, 1]) == [1, 3, 4, 7, 8, 255]
    assert merge_sort([3, 8, 4, 7, 255, 1]) == [1, 3, 4, 7, 8, 255]


test_sorts()
