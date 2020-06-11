def sum_for(lst):
    total = 0
    for item in lst:
        total += item
    return total


def sum_while(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
    return total


def sum_recursion(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursion(lst[1:])
