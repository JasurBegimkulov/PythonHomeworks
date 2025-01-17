import random

while True:
    number = random.randint(1, 100)  
    attempts = 10  

    print("Guess the number between 1 and 100! You have 10 attempts.")

    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
    else:
        print(f"You lost. Want to play again?")
        play_again = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ").strip().lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("Thanks for playing!")
            break
        continue  
    break  