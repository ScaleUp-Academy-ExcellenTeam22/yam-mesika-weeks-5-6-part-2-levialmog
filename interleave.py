def interleave(*iterables):
    """
    The function in each call sends the objects in the same location from each iterable.
    :param iterables: The iterable objects that interleave for one list.
    """
    for index in range(0, len(iterables)):
       yield [iterable[index] for iterable in iterables]
       index += 1


if __name__ == "__main__":
    interleave_list = []
    for iteration in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        interleave_list.extend(iteration)

    print(interleave_list)
