def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    count_dict1 = {}
    count_dict2 = {}

    for num in str(num1):
        if num not in count_dict1.keys():
            count_dict1[num] = 1
        else:
            count_dict1[num] = count_dict1[num] + 1
    for num in str(num2):
        if num not in count_dict2.keys():
            count_dict2[num] = 1
        else:
            count_dict2[num] = count_dict2[num] + 1

    return True if count_dict1 == count_dict2 else False
