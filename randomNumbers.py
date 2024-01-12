import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(low, high)
floatNumber = random.random()
option = random.choice(options)
random.shuffle(cards)

print(number)
print(floatNumber)
print(option)
print(cards)


guesses = 1
while True:
    guess = int(input(f"Give me your number between {low} and {high}: "))
    guesses += 1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        print(f"Correct, you guessed after {guesses} tries")
        break
