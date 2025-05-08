import random

def append_random_numbers(numbers_list, quantity=1):
    """Appends 'quantity' random floating-point numbers to numbers_list."""
    for _ in range(quantity):
        random_number = round(random.uniform(10, 100), 1)  # Random float between 10 and 100, rounded to 1 decimal place
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    """Appends 'quantity' random words to words_list."""
    word_choices = ["join", "love", "smile", "cloud", "head", "jump", "run", "laugh", "hope", "dream"]
    for _ in range(quantity):
        words_list.append(random.choice(word_choices))

def main():
    numbers = [16.2, 75.1, 52.3]
    print("numbers", numbers)
    
    append_random_numbers(numbers)
    print("numbers", numbers)
    
    append_random_numbers(numbers, 3)
    print("numbers", numbers)
    
    # Stretch challenge: working with words
    words = ["join", "love", "smile"]
    append_random_words(words, 3)
    print("words", words)

if __name__ == "__main__":
    main()
