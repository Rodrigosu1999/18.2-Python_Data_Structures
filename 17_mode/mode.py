def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_count = {}
    for num in nums:
        if num not in num_count.keys():
            num_count[num] = 1
        else:
            num_count[num] = num_count.get(num) + 1

    curr_highest = 0
    for num in num_count:
        if num_count.get(num) > curr_highest:
            curr_highest = num
    return curr_highest
