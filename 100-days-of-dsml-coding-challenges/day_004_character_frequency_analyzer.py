#character frequency analyzer------


def character_frequency_analyzer(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage:
if __name__ == "__main__":
    test_string = "hello world"
    result = character_frequency_analyzer(test_string)
    print(result)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}# This function analyzes the frequency of each character in the input string