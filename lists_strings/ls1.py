def largest_elem(lst):
    largest = None
    for item in lst:
        if largest is None or largest < item:
            largest = item
    return largest


def front_back(str):
    if len(str) > 1:
        lst = []
        lst[:0] = str
        lst[0], lst[-1] = lst[-1], lst[0]
        str = ''.join(lst)
        return str
    return str


print(front_back("cab"))
