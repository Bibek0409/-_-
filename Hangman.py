import random

# Function to choose a random word from the list
def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'code', 'challenge', 'function', 'variable']
    return random.choice(words)

# Function to display the hangman stages based on remaining tries
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        """
           -----
           |   |
           |
           |
           |
           |
        """,
        """
           -----
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

# Function to play the Hangman game
def play_game():
    word = choose_word()
    guessed = set()
    tries = 6
    guessed_word = ['_'] * len(word)

    print("Welcome to Hangman!")
    
    while tries > 0 and '_' in guessed_word:
        print(display_hangman(tries))
        print("Current word: ", ' '.join(guessed_word))
        print("Guessed letters: ", ' '.join(sorted(guessed)))
        
        guess = input("Please guess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed:
            print("You've already guessed that letter.")
            continue
        
        guessed.add(guess)
        
        # Check if the guess is correct
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = letter
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
    
    # Check if the player won or lost
    if '_' not in guessed_word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've run out of tries. The word was: {word}")

# Entry point of the program
if __name__ == "__main__":
    play_game()

