import math


def fibonacci(num):
    # num1, num2 = 0, 1
    # count = 0
    # while count < 100:
    #     print(num2)
    #     nth = num1 + num2
    #     num1 = num2
    #     num2 = nth
    #     count += 1
    if num == 2:
        return [1, 1]
    if num == 1:
        return [1]
    fib_nums = fibonacci(num - 1)
    fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return fib_nums


print(fibonacci(100))


# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# assert 3 == fib(3), fib(3)


print(math.log(354224848179261915075, 2))
