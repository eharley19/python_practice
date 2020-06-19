def rotate_list(lst):
    k = input("Rotate by: ")
    k = int(k)
    lst = lst[k:] + lst[:k]
    print(lst)


a = [1, 2, 3, 4, 5, 6]

rotate_list(a)
