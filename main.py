import random

def shuffle_numbers(number):
    number_list = list(number)
    random.shuffle(number_list)
    return ''.join(number_list)

def check_guess(guess, secret_number, show_correct_digits):
    correct_count = 0
    correct_digits = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            correct_count += 1
            if show_correct_digits:
                correct_digits.append(guess[i])
            else:
                correct_digits.append('_')
        else:
            correct_digits.append('_')
    return correct_count, ''.join(correct_digits)

def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty:\n1. Easy (3 digits)\n2. Medium (6 digits)\n3. Hard (9 digits)\nOption: ")
        if difficulty in ['1', '2', '3']:
            return int(difficulty) * 3
        else:
            print("\033[91mError: Choose a valid option (1, 2, 3).\033[0m")

def enable_green_digit():
    while True:
        green_digit = input("Do you want to enable the green digit (show correct digits)? (y/n): ")
        if green_digit.lower() in ['y', 'n']:
            return green_digit.lower() == 'y'
        else:
            print("\033[91mError: Please respond with 'y' for yes or 'n' for no.\033[0m")

def main():
    difficulty = choose_difficulty()
    show_correct_digits = enable_green_digit()
    initial_number = ''.join(map(str, range(1, difficulty + 1)))
    secret_number = shuffle_numbers(initial_number)
    attempts = 0

    print(f"Guess the {difficulty}-digit number using only the digits from 1 to {difficulty}!")

    while True:
        guess = input("Your guess: ")

        if len(guess) != difficulty:
            print(f"\033[91mError: Your guess must be exactly {difficulty} digits long.\033[0m")
            continue
        
        if len(set(guess)) != difficulty:
            print(f"\033[91mError: Your guess must contain {difficulty} unique digits.\033[0m")
            continue
        
        if any(digit not in initial_number for digit in guess):
            print(f"\033[91mError: Your guess must only contain digits from 1 to {difficulty}.\033[0m")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts!")
            break
        else:
            correct_count, correct_digits = check_guess(guess, secret_number, show_correct_digits)
            if show_correct_digits:
                print(f"{correct_count} digits correct. Correct digits: {correct_digits}. Try again.")
            else:
                print(f"{correct_count} digits correct. Try again.")

if __name__ == "__main__":
    main()
