list_length = int(input("Give me a number: "))

total = 0

for i in range(list_length):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
