import time


def average_runtime(date_structure):
    """
    The function checks 1000 times how many times the word zwitterion appears in the data structure.
    :param date_structure: List or set of words.
    :return: Run time of the function.
    """
    counter_word = 0
    start_time = time.time()

    for iteration, word in enumerate(date_structure):
        if iteration > 1000:
            return time.time() - start_time
        
        if word == "zwitterion":
            counter_word += 1


if __name__ == "__main__":
    file = open("C:\\Users\\almog\\OneDrive\\שולחן העבודה\\לימודים\\שנה ג\\סמסטר ב\\Python\\yam-mesika-weeks-5-6-part-2-levialmog\\yam-mesika-weeks-5-6-part-2-levialmog\\words.txt", "r")
    words_list = file.read().splitlines()
    words_set = set(words_list)

    print(average_runtime(words_list))
    print(average_runtime(words_set))
