def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count_dict = {}

    for char in phrase:
        if char not in letter_count_dict.keys():
            letter_count_dict[char] = 1
        else:
            letter_count_dict[char] = letter_count_dict.get(char) + 1
    return letter_count_dict
