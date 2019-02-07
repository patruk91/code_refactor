import random

larger_random_numbers = [random.randint(1, 99) for _ in range(10)]
smaller_random_numbers = [random.randint(1, 49) for _ in range(10)]


def harder_level_for_guess(user_guess):
    """
    User need to guess a number between range 1-99.
    :param user_guess: Initial define user_guess at 0, look at main.
    """
    for indice in range(1):
        while larger_random_numbers[indice] != user_guess:
            user_guess = int(input("Enter an integer from 1 to 99: "))
            check_if_correct(user_guess, larger_random_numbers, indice)


def easier_level_for_guess(user_guess):
    """
    User need to guess a number between range 1-49.
    :param user_guess: Initial define user_guess at 0, look at main.
    """
    for indice in range(len(smaller_random_numbers)):
        while smaller_random_numbers[indice] != user_guess:
            user_guess = int(input("Enter an integer from 1 to 49: "))
            check_if_correct(user_guess, larger_random_numbers, indice)


def check_if_correct(user_guess, random_numbers, indice):
    """
    Check if user numbers is correct with randomly pick up number.
    :param user_guess: Number provided by user.
    :param random_numbers: Randomly chosen number.
    :param indice: index of list with random numbers
    :return: information about if number is low, high or you guess it.
    """
    if user_guess < random_numbers[indice]:
        print("guess is low")
    elif user_guess > random_numbers[indice]:
        print("guess is high")
    else:
        print("you guessed it!")


def main():
    USER_GUESS = 0
    harder_level_for_guess(USER_GUESS)
    easier_level_for_guess(USER_GUESS)


if __name__ == '__main__':
    main()
