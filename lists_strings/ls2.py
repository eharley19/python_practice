def rev_list(l):
    l.reverse()


def reverse_list(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)
    return reversed_list

    # for i in range(0, len(lst), -1):
    #     reversed_list.append(lst[i])
    # return reversed_list


def reverse_in_place(lst):
    for i in range(len(lst)):
        lower = i
        higher = len(lst) - i - 1
        if lower < higher:
            swap(lst, lower, higher)


def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
