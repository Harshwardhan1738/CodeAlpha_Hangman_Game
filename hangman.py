import random

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
        --------
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
        --------
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
        --------
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |      
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
        --------
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        --------
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        --------
        """
    ]
    return stages[tries]

def hangman():
    word = random.choice(["PYTHON", "HANGMAN", "CODING", "DEBUG", "SCRIPT"])
    guessed, tries = set(), 6

    while tries > 0:
        print(display_hangman(tries))
        print("Word:", " ".join([l if l in guessed else "_" for l in word]))
        guess = input("Guess a letter: ").upper()

        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            guessed.add(guess)
            if all(l in guessed for l in word):
                print(f"You win! The word was {word}.")
                return
        else:
            tries -= 1
            print(f"Wrong! {tries} tries left.")

    print(f"Game over! The word was {word}.")

if __name__ == "__main__":
    hangman()
