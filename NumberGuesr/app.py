from random import randint

number = randint(1, 10)

print("Guess the the number between 1 and 10")
num = int(input())
guess = 1
guesses = []
guesses.append(num)
while num != number:
    print("Wrong, try again")
    print("Your number of guesses: " + str(guess))
    num = int(input())
    guesses.append(num)
    guess = guess + 1

    if num == number:
        print("Congratulation!")
        print("You guessed it from: " + str(guess) + " " + "guesses")
        print("Your guesses: ")
        for i in guesses:
            print(i)

