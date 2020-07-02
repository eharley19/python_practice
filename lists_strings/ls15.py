def add_num(num_lst1, num_lst2):
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
        if new_sum > 9:
            # insert new_sum's last digit to index 0 of total
            total.insert(0, new_sum % 10)
            # carry_bit is equal to 1
            carry_bit = 1

        # else
        else:
            # insert new_sum to index 0 of total
            total.insert(0, new_sum)
            # carry_bit is equal to 0
            carry_bit = 0
        offset += 1
    # return total
    return total


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


def multiply_nums(num_lst1, num_lst2):
    # create empty list for product
    product = []
    # obtain and store max_length of lists
    max_length = max(len(num_lst1), len(num_lst2))

    # while initial: offset equals 0 condition: offset is less than max_length change: offset increment + 1
    offset = 0
    while offset < max_length:
        # i  is equal to the length of num_lst1 minus the offset
        i = len(num_lst1) - offset - 1
        # j is equal to the length of num_lst2 minus the offset
        j = len(num_lst2) - offset - 1
        # element1 is 1 if i is less than 0 else element1 is the ith element of num_lst1
        element1 = 0 if i < 0 else num_lst1[i]
        # element2 is 1 if j is less than 0 else element2 is the jth element of num_lst2
        element2 = 0 if j < 0 else num_lst2[j]
        # prod is the result of element1 multiplied by element2
        prod = element1 * element2
        # if prod is greater than nine:
        if prod > 9:
            # obtain modulus 10 of prod and set to mod
            mod = prod % 10
            # insert mod to the 0 index of product
            product.insert(0, mod)
            # quo is the result of dividing prod by 10 and convert to integer
            quo = int(prod / 10)
            # insert quo to the 0 index of product
            product.insert(0, quo)
        # else
        else:
            # insert prod to the 0 index of product
            product.insert(0, prod)
        offset += 1
    # return product
    return product


def test_multiply_nums():
    assert multiply_nums([5, 5, 5], [2, 1]) == [0, 1, 0, 5]
    assert multiply_nums([1], [1]) == [1]


test_multiply_nums()
