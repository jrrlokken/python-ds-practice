def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # from collections import defaultdict
    # list = defaultdict(list)
    # result = list()
    # for char in phrase:
    #     count = 0
    # result[char].append(
    #     count
    # )
    # return result

    list = {}
    for char in phrase:
        count = phrase.count(char)
        list[char] = count
    return list
