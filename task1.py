import random

def hangman():
    # 5 predefined words
    words = ["apple", "tiger", "robot", "magic", "pizza"]
    word = random.choice(words)

    guessed = ["_"] * len(word)
    used_letters = []
    attempts_left = 6

    print("=== HANGMAN GAME ===")

    while attempts_left > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Incorrect guesses left:", attempts_left)
        print("Used letters:", ", ".join(used_letters))

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in used_letters:
            print("You already guessed that letter.")
            continue

        used_letters.append(guess)

        # Check guess
        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Wrong!")
            attempts_left -= 1

    # Win or lose message
    if "_" not in guessed:
        print("\n🎉 You guessed the word:", word)
    else:
        print("\n💀 Out of guesses! The word was:", word)

# Run the game
hangman()
