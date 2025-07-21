import random

# ----------------------------
# Constants and Word List
# ----------------------------
MAX_ATTEMPTS = 6
WORD_LIST = ["apple", "tiger", "house", "pizza", "zebra"]

# ----------------------------
# Function Definitions
# ----------------------------
def choose_word():
    """Selects a random word from the list."""
    return random.choice(WORD_LIST)

def display_word(word, guessed_letters):
    """Returns the word with guessed letters shown and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_valid_input(used_letters):
    """Prompts user for a valid, unused single letter input."""
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single alphabet letter.")
        elif guess in used_letters:
            print("⚠️ You've already guessed that letter.")
        else:
            return guess

def play_game():
    """Main function to play Hangman."""
    word_to_guess = choose_word()
    guessed_letters = set()
    wrong_attempts = 0

    print("\n🎮 Welcome to Hangman!")
    print(f"Guess the word. You have {MAX_ATTEMPTS} incorrect attempts.\n")

    while wrong_attempts < MAX_ATTEMPTS:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {MAX_ATTEMPTS - wrong_attempts}")

        guess = get_valid_input(guessed_letters)
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("✅ Correct!\n")
        else:
            wrong_attempts += 1
            print("❌ Incorrect!\n")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"🎉 Congratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"💀 Game Over. The word was: {word_to_guess}")

# ----------------------------
# Start the Game
# ----------------------------
if __name__ == "__main__":
    play_game()