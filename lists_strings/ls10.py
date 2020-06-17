def combine_lists(lst1, lst2):
    new_list = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            while i <= j:
                new_list.append(lst1[i])
                i += 1
            else:
                new_list.append(lst2[j])
                j += 1
    return new_list


a = ["h", "l", "o"]
b = ["e", "l", " "]

print(combine_lists(a, b))
