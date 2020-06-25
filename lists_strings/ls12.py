def rotate_list(lst, k):
    m = k % len(lst)
    return lst[m:] + lst[:m]
    # new_lst = []
    # m = k % len(lst)
    # i = m
    # while i < len(lst):
    #     new_lst.append(lst[i])
    #     i += 1
    # i = 0
    # while i < m:
    #     new_lst.append(lst[i])
    #     i += 1
    # return new_lst


a = [1, 2, 3, 4, 5, 6]

assert [3, 4, 5, 6, 1, 2] == rotate_list(a, 38), rotate_list(a, 38)
