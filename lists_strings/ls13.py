def fibonacci():
    num1, num2 = 0, 1
    count = 0
    while count < 100:
        print(num2)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1


fibonacci()
