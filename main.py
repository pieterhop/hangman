import random


def get_random_word():
    words = "these apples taste like flowers abracadabra flipping trampolines are fun".split()
    return words[random.randint(0, len(words) - 1)].lower()


def init_game():
    global secret
    global word_state
    global letters_tried
    global attempts

    secret = get_random_word()
    word_state = '_' * len(secret)
    letters_tried = []
    attempts = len(set(secret)) + 3


def play_game():
    init_game()
    while attempts > 0:
        guess()
        if check_win():
            print("You won!")
            print("The word I had in mind was indeed " + secret.upper() + "!")
            print("Congratulations!\n")
            break
        elif attempts == 0:
            print("You have no more attempts remaining, YOU LOSE!")
            print("The word I had in mind was... " + secret.upper() + "!")
            print("You only had " + str(word_state.count('_')) + " letters remaining...")
            print("Better luck next time!\n")
            break


def guess():
    global word_state
    global letters_tried
    global attempts
    print("The word now looks like this: " + word_state + "\n")
    if len(letters_tried) > 0:
        string_tried = ""
        for letter in letters_tried:
            if letter not in string_tried:
                string_tried += letter + " "
        print("You have tried the following letters: " + string_tried)
    print("You have " + str(attempts) + " attempts remaining.\n")
    guessed = input("Enter your guess: ").lower()
    if len(guessed) != 1 or not guessed.isalpha():
        print("Invalid guess, please enter ONE letter!\n")
        guess()
    elif guessed in letters_tried:
        print("You have already tried that letter!\n")
        guess()
    else:
        letters_tried.append(guessed)
        attempts -= 1
        indices_guessed = []
        for i, letter in enumerate(secret):
            if guessed == letter:
                indices_guessed.append(i)
        if indices_guessed:
            print("\nYou guessed a letter! It appeared " + str(len(indices_guessed)) + " time(s).")
            for index in indices_guessed:
                word_state = word_state[:index] + guessed + word_state[index + 1:]
        else:
            print("The letter you guessed didn't appear in the word.\n")
    

def check_win():
    global word_state
    if "_" not in word_state:
        return True
    return False


def ask_rematch():
    rematch = input("Do you want to play another game? Y / N\n").lower()
    while rematch not in ["y", "n"]:
        rematch = input("Do you want to play another game? Y / N\n").lower()
    if rematch == "y":
        play_game()
    elif rematch == "n":
        print("Thanks for playing Hangman, the game.\n")


def main():
    print("\nWelcome to Hangman, the game.")
    print("LET'S PLAY!\n")
    play_game()
    ask_rematch()


main()