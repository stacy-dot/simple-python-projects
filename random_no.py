import random
print("Let's play a game, where you guess a random number and i get to tell you whether you guessed right or wrong ")
random_number=random.randint(1,10)
guess=0
attempts=5 

while guess != random_number and attempts>0 :
    print(f"\nYou have {attempts} attempts left.")
    guess=int(input("Guess a number btwn 1 and 10"))
    attempts -= 1

    if random_number>guess:
        print("Too low try again")
    elif random_number<guess:
        print("Too high try again")
    else: 
        print("Yeey! You got it right")

if guess != random_number:
    print(f"\nThe correct number was {random_number}.Better luck next time!")
