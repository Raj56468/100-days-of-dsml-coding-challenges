def reverse_words(sentence):

    result = []
    word = []

    for ch in sentence:
        if ch == "":
            if word:
                result.append("".join(reversed(word)))
                word = []
        else:
            word.append(ch)
    
    if word:
        result.append("".join(reversed(word)))
    
    return " ".join(result)

if __name__ == "__main__":
    test_sentence = "Hello World"
    reversed_sentence = reverse_words(test_sentence)
    print(reversed_sentence)  
