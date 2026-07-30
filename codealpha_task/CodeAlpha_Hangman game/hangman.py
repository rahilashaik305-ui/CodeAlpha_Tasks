import random

# Predefined list of words
words = ["python", "coding", "laptop", "program", "network"]

# Choose a random word
word = random.choice(words)

guessed = set()
wrong_attempts = 0
max_attempts = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

while wrong_attempts < max_attempts:

    # Display the word
    display = ""
    completed = True

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
            completed = False

    print("\nWord:", display)
    print("Wrong Attempts Left:", max_attempts - wrong_attempts)

    if completed:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.add(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong_attempts += 1
        print("❌ Incorrect!")

if wrong_attempts == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)