import random

# Hangman ASCII art
hangman_art = {
    0: (
        "   +---+\n"
        "   |   |\n"
        "       |\n"
        "       |\n"
        "       |\n"
        "       |\n"
        "========="
    ),
    1: (
        "   +---+\n"
        "   |   |\n"
        "   O   |\n"
        "       |\n"
        "       |\n"
        "       |\n"
        "========="
    ),
    2: (
        "   +---+\n"
        "   |   |\n"
        "   O   |\n"
        "   |   |\n"
        "       |\n"
        "       |\n"
        "========="
    ),
    3: (
        "   +---+\n"
        "   |   |\n"
        "   O   |\n"
        "  /|   |\n"
        "       |\n"
        "       |\n"
        "========="
    ),
    4: (
        "   +---+\n"
        "   |   |\n"
        "   O   |\n"
        "  /|\\  |\n"
        "       |\n"
        "       |\n"
        "========="
    ),
    5: (
        "   +---+\n"
        "   |   |\n"
        "   O   |\n"
        "  /|\\  |\n"
        "  /    |\n"
        "       |\n"
        "========="
    ),
    6: (
        "   +---+\n"
        "   |   |\n"
        "   O   |\n"
        "  /|\\  |\n"
        "  / \\  |\n"
        "       |\n"
        "========="
    )
}

words = (
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "database",
    "internet"
)

word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0

print("----- HANGMAN -----")

while wrong_guesses < 6:

    print()
    print(hangman_art[wrong_guesses])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        wrong_guesses += 1

    if all(letter in guessed_letters for letter in word):
        print("\n" + hangman_art[wrong_guesses])
        print(f"\n🎉 You win! The word was: {word}")
        break

else:
    print("\n" + hangman_art[wrong_guesses])
    print(f"\n💀 You lose! The word was: {word}")