def selection_sort(lst):
    lst_length = range(len(lst) - 1)
    for i in lst_length:
        min_val = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_val]:
                min_val = j
        if min_val != i:
            lst[min_val], lst[i] = lst[i], lst[min_val]
    return lst


def insertion_sort(lst):
    lst_length = range(1, len(lst))
    for i in lst_length:
        while lst[i - 1] > lst[i] and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i - 1
    return lst


a = [3, 8, 4, 7, 255, 1]
