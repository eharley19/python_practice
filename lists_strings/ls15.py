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
    # obtain and store max_length of lists
    # while initial: offset is 0; condition: offset is less than max_length of lists, change: offset increments +1
