def get_perfect_divided():
    """
    The function checks infinitely if numbers are perfect numbers to divide.
    :return: The number which is a perfect division.
    """
    checked_number = 2
    while True:
        if checked_number == sum((num for num in range(1, int(checked_number / 2) + 1) if checked_number % num == 0)):
            yield checked_number
        checked_number += 1


if __name__ == "__main__":
    for number in get_perfect_divided():
        print(number)
