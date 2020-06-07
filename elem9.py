from random import randint

x = randint(1,50)

num = int(input("I'm thinking of a number between 1 and 50. Guess? "))

guesses = 0

while guesses < 9:
    if num == x:
        print("You got it!")
        break
    elif num < x:
        print("Higher!")
        guesses += 1
        print("Number of times guessed: ",guesses)
        num = int(input("Guess again: "))
    elif num > x:
        print("Lower!")
        guesses += 1
        print("Number of times guessed: ",guesses)
        num = int(input("Guess again: "))
else:
    print("Sorry, you're out of guesses.")
    
