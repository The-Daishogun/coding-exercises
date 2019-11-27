def change_words(word):
    word = word.lower()
    total = 1
    for char in word:

        if char == "l" or char == "f":
            total *= 2
        elif char == "d":
            total *= 2
        elif char == "t":
            total *= 2

    return total


print(change_words(input()))
