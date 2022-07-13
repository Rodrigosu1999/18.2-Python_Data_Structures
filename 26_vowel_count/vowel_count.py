def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    low_case_phrase = phrase.lower()
    count = {}

    for char in low_case_phrase:
        if char in vowels:
            if char not in count.keys():
                count[char] = 1
            else:
                count[char] = count[char] + 1
    return count
