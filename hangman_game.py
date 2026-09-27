import random

# List of words
words = ["python", "computer", "developer", "database", "coding"]

# Hints for each word
hints = {
    "python": "A programming language",
    "computer": "An electronic machine",
    "developer": "A person who creates software",
    "database": "Stores information",
    "coding": "Writing computer programs"
}

# Choose a random word
word = random.choice(words)

# Get the hint for the selected word
hint = hints[word]

# Create blanks
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of chances
chances = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

print("Guess the word one letter at a time.")
print("You have 6 wrong chances.")
print("Hint:", hint)

while chances > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong chances left:", chances)

    letter = input("Enter a letter: ").lower()

    # Check if user entered only one letter
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if letter in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(letter)

    # Check the letter
    if letter in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter

    else:
        print("Wrong guess!")
        chances = chances - 1

# Check the result
if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n😢 Game Over!")
    print("The correct word was:", word)