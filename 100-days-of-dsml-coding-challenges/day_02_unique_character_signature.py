def is_unique(s: str) -> bool:
    """
    Check if all characters in the string are unique.

    Args:

    s (str): The input string to check.

    Returns:

    bool: True if all characters are unique, False otherwise.
    """
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

def first_repeated_character(s: str) -> str:
    """
    Find the first repeated character in the string.

    Args:

    s (str): The input string to check.

    Returns:

    str: The first repeated character, or an empty string if none found.
    """
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return ""

def unique_count(s: str) -> int:
    """
    Count the number of unique characters in the string.

    Args:

    s (str): The input string to check.

    Returns:
    
    int: The count of unique characters.
    """
    return len(set(s))

if __name__ == "__main__":
    test_string = "swiss"
    print(f"Is '{test_string}' unique? {is_unique(test_string)}")
    print(f"First repeated character in '{test_string}': '{first_repeated_character(test_string)}'")
    print(f"Number of unique characters in '{test_string}': {unique_count(test_string)}")