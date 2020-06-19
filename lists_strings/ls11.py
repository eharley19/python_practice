def sorted_list(lst1, lst2):
    new_list = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if j >= len(lst2) or i < len(lst1) and lst1[i] <= lst2[j]:
            new_list.append(lst1[i])
            i += 1
        else:
            new_list.append(lst2[j])
            j += 1
    return new_list


a = [12, 26, 38]
b = [4, 35, 48]

print(sorted_list(a, b))
