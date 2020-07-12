def add_num(num_lst1, num_lst2, base=10):
    # intitialize total to empty list
    total = []
    # carry_bit is equal to 0
    carry_bit = 0
    # set max_length
    max_length = max(len(num_lst1), len(num_lst2))

    # while initial: offset is 0, condition: offset is less than max_length, change: offset increments + 1
    offset = 0
    while offset < max_length:

        # i is length of num_lst1 minus offset
        i = len(num_lst1) - 1 - offset
        # j is length of num_lst2 minus offset
        j = len(num_lst2) - 1 - offset
        # if i is less than 0
        element1 = 0 if i < 0 else num_lst1[i]
        # if j is less than 0
        element2 = 0 if j < 0 else num_lst2[j]

        # set to new_sum to the  sum of element1 and element2 and carry_bit
        new_sum = element1 + element2 + carry_bit
        # if new_sum greater than 9
        if new_sum > base - 1:
            # insert new_sum's last digit to index 0 of total
            total.insert(0, new_sum % base)
            # carry_bit is equal to 1
            carry_bit = 1

        # else
        else:
            # insert new_sum to index 0 of total
            total.insert(0, new_sum)
            # carry_bit is equal to 0
            carry_bit = 0
        offset += 1
    if carry_bit == 1:
        total.insert(0, carry_bit)
    # return total
    return total


def test_add_num():
    assert add_num([1], [1]) == [2]
    assert add_num([2, 3], [1]) == [2, 4]
    assert add_num([1], [3, 2]) == [3, 3]
    assert add_num([9], [2]) == [1, 1]
    assert add_num([0], [1], 2) == [1]
    assert add_num([3], [1, 1], 4) == [2, 0]


def subtract_nums(num_lst1, num_lst2):
    # create empty list for difference
    difference = []
    # intialize borrow_flag equal to 0
    borrow_flag = 0
    # obtain and store max_length of lists
    max_length = max(len(num_lst1), len(num_lst2))
    # while initial: offset is 0; condition: offset is less than max_length of lists, change: offset increments +1
    offset = 0
    while offset < max_length:
        # i is the length of num_lst1 minus offset
        i = len(num_lst1) - offset - 1
        # j is the length of num_lst2 minus offset
        j = len(num_lst2) - offset - 1
        # diff is  the result of subtracting j-th element of num_lst2 (element2) from i-th element of num_lst1 (element1) minus borrow_flag
        element1 = 0 if i < 0 else num_lst1[i]
        element2 = 0 if j < 0 else num_lst2[j]
        diff = element1 - element2 - borrow_flag
        # if diff less than zero
        if diff < 0:
            # add 10 to diff
            diff += 10
            # borrow_flag is equal to 1
            borrow_flag = 1
            # insert diff to index 0 of difference
            difference.insert(0, diff)
        # else
        else:
            # insert diff to index 0 of difference
            difference.insert(0, diff)
            # borrow_flag is equal to 0
            borrow_flag = 0
        offset += 1
    if borrow_flag == 1:
        difference = [digit * -1 % 10 for digit in difference]
        difference.insert(0, "-")
    # return difference
    return difference


def multiply_nums(num_lst1, num_lst2, base=10):

    sub_products = []

    for z, elem1 in enumerate(reversed(num_lst1)):
        carry = 0
        sub_products.append([0] * z)
        for elem2 in reversed(num_lst2):
            res = elem1 * elem2 + carry
            res1 = res % base
            sub_products[-1].insert(0, res1)
            carry = res // base
        if carry:
            sub_products[-1].insert(0, carry)

    sum = [0]
    for sub_product in sub_products:
        sum = add_num(sum, sub_product, base)
    return sum


# a = ['a', 'b', 'c']
# b = [1, 2, 3, 4]
# c = [0]
# d = []
# e = [[0, 1], [3, 5, 6, 7], [8]]

# multiply_nums(b, b)

test_add_num()


def test_multiply_nums():
    assert multiply_nums([5, 5, 5], [2, 1]) == [1, 1, 6, 5, 5]
    assert multiply_nums([2, 1], [5, 5, 5]) == [1, 1, 6, 5, 5]
    assert multiply_nums([1], [1]) == [1]
    assert multiply_nums([0], [1], 2) == [0]
    assert multiply_nums([2], [4], 5) == [1, 3]
    assert multiply_nums([1, 2], [2], 3) == [1, 0, 1]


test_multiply_nums()
