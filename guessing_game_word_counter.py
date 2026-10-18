import random
import re
from collections import Counter

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 5
MAX_SCORE=100
SCORE_DEDUCTION=10
TOP_WORDS=10

def get_integer(message, minimum=None, maximum=None):
    while True:
        try:
            number = int(input(message))
            if minimum is not None and number < minimum:
                print(f"Input must be a positive integer.")
                continue

            if maximum is not None and number > maximum:
                print(f"Input must be an integer between {minimum} and {maximum}.")
                continue
            return number
        
        except ValueError:
            print("Invalid input. Please enter an integer.")

def play_gussing_game():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts=0

    print("\n==== Welcome to the Guessing Game! ====")
    print(f"Guess the secret number between {MIN_NUMBER} and {MAX_NUMBER}. You have {MAX_ATTEMPTS} attempts.")
    
    while attempts<MAX_ATTEMPTS:
        guess=get_integer(f"Attempt {attempts+1}: Enter your guess: ", MIN_NUMBER, MAX_NUMBER)
        attempts += 1

        if guess==secret_number:
            score=MAX_SCORE-(attempts-1)*SCORE_DEDUCTION
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts.")
            print(f"Your score is: {score}")
            break

        elif guess<secret_number:
             print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

    print("\nGame over! You have used all your attempts.")
    print("The correct number was:", secret_number)
    print("Your Score: 0")


import re
from collections import Counter


def count_words():
    print("\n--- Word Counter ---")

    file_name = input(
        "Enter the name of the text file (with .txt extension): "
    ).strip()

    if not file_name:
        print("File name cannot be empty.")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as text_file:
            text = text_file.read()

    except FileNotFoundError:
        print("File not found! Please check the file name and try again.")
        return

    except (OSError, UnicodeError):
        print("Unable to read the file. Please check the file and try again.")
        return

    # Convert all text to lowercase and extract words without punctuation
    words = re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())

    # Count the frequency of each word
    word_counts = Counter(words)

    print("\n--- Word Count Results ---")
    print("Total words:", len(words))
    print("Unique words:", len(word_counts))

    if not words:
        print("The file is empty or contains no recognizable words.")
        return

    print("\nMost Common Words:")

    for word, frequency in word_counts.most_common(10):
        print(f"{word}: {frequency}")

def main():
    while True:
        print("\n==== Main Menu ====")
        print("1. Play Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = get_integer("Enter your choice (1-3): ", 1, 3)

        if choice == 1:
            play_gussing_game()
        elif choice == 2:
            count_words()
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()