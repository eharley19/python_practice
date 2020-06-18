def on_all(lst, func):
    return [func(element) for element in lst]


print(on_all(range(1, 21), lambda x: x * x))
