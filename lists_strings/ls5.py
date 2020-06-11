
def running_total(lst):
    total = 0
    running_total_list = []
    for item in lst:
        total += item
        running_total_list.append(total)
    return running_total_list


test_list = [1, 2, 3, 4, 5]

assert [1, 3, 6, 10, 15] == running_total(test_list)
