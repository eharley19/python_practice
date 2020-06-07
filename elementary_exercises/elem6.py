list_length = int(input("Give me a number: "))

choice = input("Product or Sum? ")

product = 1

tot = 0

for i in range(1, list_length):
    product *= i
    tot += i

if choice == "Product":
    print("The product is ", product)
elif choice == "Sum":
    print("The sum is ", tot)
else:
    print("That is not a valid choice.")
