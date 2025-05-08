
def main():
    pass
"""This is to design a game where the user will guess a number 
"""
secret_number = 9
guess_count = 0
guess_limit = 3
attempt = 0
while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    if guess == secret_number:
        print("You won")
        print({f"You guessed the number in {attempt} attempts"})
        break
    else:
        attempt += 1
        print("You have used", attempt, "attempts")
        if attempt == guess_limit:
            print("You lose")
            break


main()