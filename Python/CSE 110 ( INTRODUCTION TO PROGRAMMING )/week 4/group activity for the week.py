#importing randoms
import random
numbers = random.randint(1,100)
number_correct = int(numbers)
attempts = 0
play_again = "yes"


while play_again == "yes":
   
    guess_number = int(input("What is the your guess? "))
    while number_correct != guess_number:
        guess_number = int(input("What is the your guess? "))
        attempts += 1
        
        if number_correct == guess_number:
         print("You guessed right")
         break
        elif number_correct < guess_number:
            print("lower")
        elif number_correct > guess_number:
           print("Higher")
    else:
        print("Unknown")
        print()
    print(f"number of attempts: {attempts}")

    play_again = input("Will you like to play again? (yes/no) ")


