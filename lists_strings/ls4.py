def odd_elem(lst):
    odd_elements = []
    for i in range(len(lst)):
        if i % 2 != 0:
            odd_elements.append(lst[i])
    return odd_elements


# lst[1::2]
