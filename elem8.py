bottom = 1
top = 100

for num in range(bottom, top + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)