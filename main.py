# Function to check if the player has guessed all the letters in the secret word
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


# Function to display the current state of the secret word with guessed letters revealed
def show_hidden_word(secret_word, old_letters_guessed):
    revealed_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            revealed_word += secret_word[i]
        else:
            revealed_word += '_'

    print(revealed_word)


# Function to check if the input letter is valid
def check_valid_input(letter_guessed, old_letters_guessed):
    if letter_guessed in old_letters_guessed or len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    return True


# Function to update the list of guessed letters with the new guess
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    return False


# Function to choose a random word from a file
def choose_word(file_path, index):
    try:
        with open(file_path, "r") as input_file:
            text = input_file.read()
            words = text.split()
            secret_word = words[index]
            num_of_words = len(set(words))
        return (num_of_words, secret_word)
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return (0, "")
    except IndexError:
        print(f"Error: The index {index} is out of range.")
        return (0, "")
    except Exception as e:
        print("Invalid input. Please try again.")
        return (0, "")


# Function to print the hangman image corresponding to the number of tries
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {0: """
     x-------x
    """,

                      1: """
     x-------x
     |
     |
     |
     |
     |
    """,

                      2: """
     x-------x
     |       |
     |       0
     |
     |
     |
    """,

                      3: """
     x-------x
     |       |
     |       0
     |       |
     |
     |
    """,

                      4: """
     x-------x
     |       |
     |       0
     |      /|\
     |
     |
    """,

                      5: """
     x-------x
     |       |
     |       0
     |      /|\\
     |      /
     |
    """,

                      6: """
     x-------x
     |       |
     |       0
     |      /|\\
     |      / \\
     |
    """}
    print(HANGMAN_PHOTOS[num_of_tries])


# Function to print the list of old guessed letters
def print_old_letter_guessed(old_letter_guessed):
    old_letter_str = " -> ".join(old_letter_guessed)
    print(old_letter_str)


def main():
    MAX_TRIES = 6
    num_of_tries = 0
    old_letters_guessed = []

    print("""      _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/
6""")
    print("Let’s start!")

    valid_input = False
    secret_word = ""


#path and index handling
    while not valid_input:
        try:
            path = input("Enter file path: ")
            index = int(input("Enter index: "))
            result = choose_word(path, index)
            if result[0] > 0:
                valid_input = True
                secret_word = result[1]
            else:
                print("Invalid input. Please try again.")

        except ValueError:
            print("Invalid index. Please enter a valid integer.")
        except Exception as e:
            print("Invalid input. Please try again.")


#Main Game
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
        letter_guessed = input("Guess a letter:").lower()

        while not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            letter_guessed = input("Guess a letter:").lower()

        if letter_guessed not in secret_word:
            print(":(")
            num_of_tries += 1

        print_old_letter_guessed(old_letters_guessed)

    if not check_win(secret_word, old_letters_guessed):
        print("LOSE the word was: "+secret_word)
    else:
        print("WIN")


if __name__ == "__main__":
    main()
