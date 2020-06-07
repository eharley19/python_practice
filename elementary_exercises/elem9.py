from random import randint


x = randint(1, 1024)

print("I'm thinking of a number between 1 and 1024.")

prev_num = None

guesses = 1

while guesses < 11:
    num = int(input("Guess: "))
    if num == prev_num:
        print("You've already guessed that.")
        num = int(input("Guess again: "))
        guesses -= 1
        continue

    if num == x:
        print("You got it!")
        break
    elif num < x:
        print("Higher!")

    elif num > x:
        print("Lower!")

    print("Number of times guessed: ", guesses)
    prev_num = num
    guesses += 1
else:
    print("Sorry, you're out of guesses.")
