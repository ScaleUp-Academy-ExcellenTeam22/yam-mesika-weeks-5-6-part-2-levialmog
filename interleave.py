def interleave(*iterables):
    """
    The function gets iterables, in each call sends the items in the same index.
    :param iterables: The iterable objects to be interleaved for one list.
    :return: A list of items in the same index from iterables.
    """
    for item in range(0, len(iterables)):
        yield [iterable[item] for iterable in iterables]
        item += 1


if __name__ == "__main__":
    interleave_list = []
    for iteration in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        interleave_list.extend(iteration)

    print(interleave_list)
