def combine_lists(lst1, lst2):
    new_list = []
    for elem1, elem2 in zip(lst1, lst2):
        new_list.append(elem1)
        new_list.append(elem2)
    return new_list


a = ["h", "l", "o"]
b = ["e", "l", " "]

assert list("hello ") == combine_lists(a, b)
