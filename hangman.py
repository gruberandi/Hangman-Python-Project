import json
import random
import string

with open('word.json', 'r') as file:
    words_data = json.load(file)

words = words_data["data"]

def get_random_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman(wrong_character_number):
    word = get_random_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    missed_letters_number = 0
    allow_wrong_character = wrong_character_number


    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while missed_letters_number < allow_wrong_character:
        word_display = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_display))
        print("Used letters: ", " ".join(sorted(used_letters)))
        print(f"you can only make {allow_wrong_character - missed_letters_number} mistake")

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! {user_letter} is in the word.")
            else:
                print(f"Oops! {user_letter} is not in the word.")
                missed_letters_number +=  1
        elif user_letter in used_letters:
            print("You have already guessed that letter. Try again.")
        else:
            print("Invalid character. Please guess a letter.")


    print(f"You loose, the word was : {word}")


hangman(10)
