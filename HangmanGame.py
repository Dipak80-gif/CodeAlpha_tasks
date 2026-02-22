import random

# Predefined word list
words = ["python", "apple", "chair", "robot", "music"]

# Pick a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses. Let's start!")

while wrong_guesses < max_wrong:
    # Display current word progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check for win
    if "_" not in display:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(" You already guessed that letter.")
    elif guess in word:
        print(" Good guess!")
        guessed_letters.append(guess)
    else:
        print(" Wrong guess.")
        guessed_letters.append(guess)
        wrong_guesses += 1
        print(f"Remaining guesses: {max_wrong - wrong_guesses}")

# Loss condition
if wrong_guesses == max_wrong:
    print("\n Game Over!")
    print("The word was:", word)
