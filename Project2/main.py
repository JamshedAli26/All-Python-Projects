import random
num = random.randint(1, 100)
total_try = 0
while num > -1:
    guess = int(input("Ente your guess here: "))
    if guess < num:
        total_try += 1
        print(f"Total try: {total_try}")
        print(f"You guess {guess}\nguess higher number please.")
    elif guess > num:
        total_try += 1
        print(f"Total try: {total_try}")
        print(f"you guess {guess}\nguess lower number please.")
    elif guess == num:
        print(f"You guess {guess} Congratulation you guess the number correctly in {total_try} tries")
        break

