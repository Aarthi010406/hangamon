import random

WORDS = ["python", "hangman", "keyboard", "program", "network"]
MAX_WRONG = 6


def show_status(word, guessed, wrong_count):
    """Print the word with blanks, wrong guesses left, and letters tried."""
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Wrong guesses left:", MAX_WRONG - wrong_count)
    print("Letters tried:", " ".join(sorted(guessed)) if guessed else "none")


def play():
    word = random.choice(WORDS)
    guessed = []        # every letter the player has tried
    wrong_count = 0

    print("=== HANGMAN ===")
    print(f"Guess the {len(word)}-letter word. You can miss {MAX_WRONG} times.")

    while wrong_count < MAX_WRONG:
        show_status(word, guessed, wrong_count)

        # Win check: every letter of the word has been guessed
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
        if won:
            print(f"\nYou win! The word was '{word}'.")
            return

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already tried that letter.")
        else:
            guessed.append(guess)
            if guess in word:
                print("Good guess!")
            else:
                wrong_count += 1
                print("Nope, that letter isn't in the word.")

    print(f"\nGame over! The word was '{word}'.")


if __name__ == "__main__":
    play()
