#Task 9.1. Module 8 (HW-01)
"""Guess-number game
IA choses the number and then guesses itself
"""

import numpy as np


def random_predict(number:int=1) -> int:
    """Guessing random number in less than 20 attempts

    Args:
        Number (int, optional): Generated number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    attempts_count = 0
    beginning_number = 1
    ending_number = 1001

    while attempts_count < 21: # the game ends if we exceed 20 attempts
        attempts_count+=1
        predict_number = int((beginning_number+ending_number) / 2)

        if predict_number > number:
            ending_number = predict_number

        elif predict_number < number:
            beginning_number = predict_number

        else:
            break # end of the game as the number is guessed succesfully 
    return attempts_count


def score_game(random_predict) -> int:
    """How many attempts in average is required to guess 1000 different numbers

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    random_array = np.random.randint(1, 1001, size=(1000))  # generated 1000 numbers from 1 to 1000

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorythm finds the number using {score} attempts in average")
    return(score)

if __name__ == '__main__':    
    # RUN
    score_game(random_predict)