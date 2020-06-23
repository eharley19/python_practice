def largest_elem(lst):
    largest = None
    for item in lst:
        if largest is None or largest < item:
            largest = item
    return largest
