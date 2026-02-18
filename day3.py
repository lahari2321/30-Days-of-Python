import random

print("Welcome to Number Guessing Game!...")
print("Guess the number between 1 to 100:---")
select_number = random.randint(1,100)
attempts=0
while True:
    guess=int(input("Enter your guess:  "))
    attempts+=1
    
    if select_number>guess:
        print("Too low! Try again")
    elif select_number<guess:
        print("Too high!,Try again")
    else:
        print(f"🥳Congratulations! You guessed the correct number") 
        print(f'attempts:- {attempts}')
        break
