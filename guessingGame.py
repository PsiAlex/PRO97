import random
print("number guessing game")
number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("enter your guess"))

    if guess == number:
        print("Congratulations, You Won!")
        break

    elif guess < number:
        print("Your guess was too low")
    
    else:
        print("Your guess was too high")

    chances += 1

if not chances < 5:
    print("You Lose, The Number Is: ", number)