def sorted_list(lst1, lst2):
    new_list = lst1 + lst2
    new_list.sort()
    return new_list


a = [12, 26, 38]
b = [4, 35, 48]

print(sorted_list(a, b))