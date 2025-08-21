import random

words = ["python", "hangman", "coding", "program", "computer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to hangman!")
print("Guess the word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter!")
        continue
    used_letters.append(guess)
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f" Wrong! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))
    print("Used letters:", " ".join(used_letters))

if "_"not in guessed:
    print("\n Congratulations! You guessed the word:",word)
else:
    print("\n Game Over! The word was:", word)
