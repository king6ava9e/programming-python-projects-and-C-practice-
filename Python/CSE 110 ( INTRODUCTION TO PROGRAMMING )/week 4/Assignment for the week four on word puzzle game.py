#secret code
secret = "patience"
attempt = 0

print("Welcome to word wordle game! ")
#Displaying underscores for each letter in the secret word
hint = "_" * len(secret)
print(f"Your hint is : {hint.strip()}")
print()
guess = input("What is your guess? ").lower()

#validating the guess
while True:
    guess = input("What is your guess? ").lower()
    attempt += 1
    if not len(guess) == len(secret):
        print(f"Your guess must have {len(secret)} letters. Try again.")
    elif guess == secret:
        print(f"Congratulations! You've guessed {attempt} times.")
        break
    else:
        hint = ""
       
        
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                hint += guess[i].upper()
            elif guess[i] in secret:
                hint += guess[i].lower()
            else:
                hint += "_"
        print("Your hint is : ", " ".join(hint))
     