from ls15 import multiply_nums, subtract_nums


def base_converter(num_lst, start_base, tar_base):

    # determine highest place
    power = 0
    while compare(pow_base(start_base, tar_base, power), num_lst) <= 0:
        power += 1
    highest_place = power - 1
    # initialize digits as empty list
    digits = []
    remainder = num_lst
    # for place in highest place to lowest place:
    for place in range(highest_place, -1, -1):
        # calculate digit
        remainder, digit = calculate_remainder_and_digit(remainder, start_base, tar_base, place)
        # append digit to digits list
        digits.append(digit)
    return digits


def calculate_remainder_and_digit(num_lst, start_base, tar_base, place):
    remainder = num_lst
    quotient = 0
    divisor = pow_base(start_base, tar_base, place)
    while compare(remainder, divisor) >= 0:
        remainder = subtract_nums(remainder, divisor, start_base)
        quotient += 1
    return remainder, quotient


def pow_base(tar_base, base, power):
    result = [1]
    base_list = convert_to_list(base, tar_base)
    for _ in range(power):
        result = multiply_nums(base_list, result, tar_base)
    return result


def convert_to_list(num, base):
    # determine highest place
    if num == 0:
        return [0]
    power = 0
    places = []
    while base ** power <= num:
        places.append(base**power)
        power += 1
    # del places[-1]
    # initialize digits as empty list
    digits = []
    remainder = num
    # for place in highest place to lowest place:
    for place in reversed(places):
        digit = remainder // place
        remainder -= digit * place
        # append digit to digits list
        digits.append(digit)
    return digits


def compare(num_lst1, num_lst2):
    diff = subtract_nums(num_lst1, num_lst2)
    if '-' in diff:
        return - 1
    elif not any(diff):
        return 0
    else:
        return 1

# test_base_converter()
