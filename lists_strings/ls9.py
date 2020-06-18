def concatenate_list(lst1, lst2):
    return lst1 + lst2


alpha = ["a", "b", "c", "d"]
num = [1, 2, 3, 4]

assert ["a", "b", "c", "d", 1, 2, 3, 4] == concatenate_list(alpha, num)
