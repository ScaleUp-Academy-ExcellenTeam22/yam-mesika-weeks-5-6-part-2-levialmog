def get_perfect_divided(upper_bound=10000):
    """
    The function checks each number from 1 to the upper_bound if it is a perfect number to divide. With the help of
    a generator and a sum function.
    :param upper_bound: A number that defines the upper bound of the numbers that returns from the generator,
    so that the function does not run indefinitely.
    :return: In each round in loop, the number which is a perfect division.
    """
    for checked_number in range(1, upper_bound):
        if checked_number == sum((num for num in range(1, int(checked_number / 2) + 1) if checked_number % num == 0)):
            yield checked_number


if __name__ == "__main__":
    for number in get_perfect_divided():
        print(number)
